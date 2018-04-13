import csv
import time

from django.conf import settings
from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from revolv.base.models import RevolvUserProfile
from revolv.base.users import UserDataMixin
from revolv.base.utils import ProjectGroup
from revolv.base.views import BaseStaffDashboardView
from revolv.project.models import Project, ProjectMatchingDonors
from revolv.payments.models import Payment, PaymentType


class AdministratorDashboardView(BaseStaffDashboardView):
    """
    Basic view for the Administrator dashboard. Shows the list of projects that this
    ambassador owns. Also, shows drafted projects.
    """
    template_name = 'base/dashboard.html'
    role = "admin"

    def get_context_data(self, **kwargs):
        context = super(AdministratorDashboardView, self).get_context_data(**kwargs)
        context["donated_amount"] = self.request.session.get('amount')
        context["donated_project"] = self.request.session.get('project')
        context["cover_photo"] = self.request.session.get('cover_photo')
        context["url"] = self.request.session.get('url')
        context["social"] = self.request.session.get('social')
        if self.request.session.get('social'):
            del self.request.session['social']
        amount = self.user_profile.reinvest_pool + self.user_profile.solar_seed_fund_pool
        if self.user_profile and amount > 0.0:
            context["reinvestment_amount"] = self.user_profile.reinvest_pool + self.user_profile.solar_seed_fund_pool
        else:
            context["reinvestment_amount"] = 0.0
        context["project_dict"][ProjectGroup('Drafted Projects', "drafted")] = Project.objects.get_drafted()
        return context


class AdministratorEmailView(UserDataMixin, TemplateView):
    """View for the list of newsletter subscribers for the dashboard.
    """
    template_name = 'administrator/email.html'

    def get_context_data(self, **kwargs):
        context = super(AdministratorEmailView, self).get_context_data(**kwargs)

        user_profiles = RevolvUserProfile.objects.get_subscribed_to_newsletter()
        user_emails = list(user_profiles.values_list("user__email", flat=True))

        context['subscribed_user_emails'] = user_emails
        return context


def admin_email_csv_download(request):
    """View for downloading the list of newsletter subscribers as a csv file.
    Accessed via AdministratorEmailView.
    """
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="emails.csv"'

    users_subscribed = RevolvUserProfile.objects.get_subscribed_to_newsletter()
    newsletter_rows = [(u.user.email, u.user.first_name, u.user.last_name, u.user.date_joined) for u in
                       users_subscribed]

    writer = csv.writer(response)
    writer.writerow(['Email', 'FirstName', 'LastName', 'DateJoined'])
    writer.writerows(newsletter_rows)

    return response


class AdminManualPaymentView(UserDataMixin, TemplateView):
    template_name = 'administrator/manual_payment.html'

    def get_context_data(self, **kwargs):
        context = super(AdminManualPaymentView, self).get_context_data(**kwargs)
        context["active_projects"] = Project.objects.get_active()
        return context

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            project_id = request.POST.get("project_id")
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            amount = request.POST.get("amount", 0)
            amount = float(amount)

            project = get_object_or_404(Project, pk=project_id)

            if project:
                if first_name and last_name:
                    last_name_part = last_name[0:1] + str(int(time.time() * 1000))[6:13]
                    email = first_name + "." + last_name_part + "@re-volv.org"
                    username = first_name[0:15] + last_name_part
                    password = "revolv123"
                    user = User.objects.create_user(username, email, password, first_name=first_name,
                                                    last_name=last_name)
                    user = user.revolvuserprofile
                else:
                    user_id = User.objects.get(username='Anonymous').pk
                    user = RevolvUserProfile.objects.get(user_id=user_id)

                try:
                    admin = RevolvUserProfile.objects.get(user__username=settings.ADMIN_PAYMENT_USERNAME)
                except RevolvUserProfile.DoesNotExist:
                    admin = user

                payment = Payment.objects.create(
                    user=user,
                    entrant=admin,
                    amount=amount,
                    project=project,
                    tip=None,
                    payment_type=PaymentType.objects.get_check(),
                )

                project_matching_donors = ProjectMatchingDonors.objects.filter(project=project, amount__gt=0)
                if project_matching_donors:
                    for donor in project_matching_donors:
                        if donor.amount > amount:
                            matching_donation = amount
                            donor.amount = donor.amount - amount
                            donor.save()
                        else:
                            matching_donation = donor.amount
                            donor.amount = 0
                            donor.save()

                        Payment.objects.create(
                            user=donor.matching_donor,
                            entrant=donor.matching_donor,
                            amount=matching_donation,
                            project=project,
                            tip=None,
                            payment_type=PaymentType.objects.get_check(),
                        )

            data["success"] = True
            data["message"] = "Saved manual payment successfully."
        except Exception:
            data["success"] = False
            data["message"] = "Error while saving manual payment."

        return JsonResponse(data)
