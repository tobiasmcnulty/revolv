from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.db.models import Sum

from django.shortcuts import get_object_or_404
from revolv.base.users import UserDataMixin
from revolv.base.utils import ProjectGroup
from revolv.payments.models import Payment
from revolv.project.models import Project, Category
from revolv.project.utils import aggregate_stats

from revolv.payments.models import UserReinvestment


def humanize_int(n):
    # NOTE: GPL licensed snipped c/o
    # https://github.com/localwiki/localwiki-backend-server/blob/master/localwiki/users/views.py#L47
    mag = 0
    if n < 10000:
        return int(n)
    while n>= 10000:
        mag += 1
        n /= 1000.0
    return '%.1f%s' % (n, ['', 'k', 'M', 'B', 'T', 'P'][mag])


def humanize_integers(d):
    for k in d:
        d[k] = humanize_int(int(d[k]))

def total_donations(profile):
    project = get_object_or_404(Project, title='Operations')
    payments = Payment.objects.filter(entrant=profile, user=profile).exclude(project=project)
    if payments:
        return payments.aggregate(Sum('amount'))['amount__sum']
    else:
        return 0

class DonorDashboardView(UserDataMixin, TemplateView):
    """
    Basic view for the Donor dashboard.
    """
    template_name = 'base/dashboard.html'

    def dispatch(self, request, *args, **kwargs):
        if "password_change_success" in request.GET.keys():
            messages.success(request, "Awesome! Your password has been successfully changed.")

        return super(DonorDashboardView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DonorDashboardView, self).get_context_data(**kwargs)

        project_dict = {}
        project_dict[ProjectGroup('My Projects', "donated")] = Project.objects.donated_projects(self.user_profile)
        context["project_dict"] = project_dict

        active = Project.objects.get_active()
        context["first_project"] = active[0] if active.count() > 0 else None
        context["role"] = "donor"
        context["donated_amount"] = self.request.session.get('amount')
        context["donated_project"] = self.request.session.get('project')
        context["cover_photo"] = self.request.session.get('cover_photo')
        context["url"] = self.request.session.get('url')
        context["social"] = self.request.session.get('social')
        if self.request.session.get('social'):
            del self.request.session['social']
        context["donor_has_no_donated_projects"] = Project.objects.donated_projects(self.user_profile).count() == 0

        context['donated_projects'] = Project.objects.donated_projects(self.user_profile)
        statistics_dictionary = aggregate_stats(self.user_profile)
        statistics_dictionary['total_donated'] = total_donations(self.user_profile)
        total_people_affected = Project.objects.donated_completed_projects(self.user_profile)
        statistics_dictionary['people_served'] = total_people_affected
        humanize_integers(statistics_dictionary)
        admin_reinvestment = \
            Payment.objects.filter(user=self.user_profile).filter(admin_reinvestment__isnull=False).aggregate(
                Sum('amount'))[
                'amount__sum'] or 0
        user_reinvestment = UserReinvestment.objects.filter(user=self.user_profile).aggregate(Sum('amount'))[
                                'amount__sum'] or 0
        statistics_dictionary['reinvestment'] = admin_reinvestment + user_reinvestment
        context['statistics'] = statistics_dictionary
        amount = self.user_profile.reinvest_pool + self.user_profile.solar_seed_fund_pool
        if self.user_profile and amount > 0.0:
            context["reinvestment_amount"] = self.user_profile.reinvest_pool + self.user_profile.solar_seed_fund_pool
        else:
            context["reinvestment_amount"] = 0.0

        # context['category_setter_url'] = reverse('dashboard_category_setter')
        # context['categories'] = Category.objects.all().order_by('title')
        # context['preferred_categories'] = self.user_profile.preferred_categories.all()

        return context