from django.contrib import admin

from .models import Category, DonationLevel, Project, ProjectUpdate, AnonymousUserDetail, StripeDetails

class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal = ('ambassadors',)

admin.site.register(Category)
admin.site.register(DonationLevel)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectUpdate)
admin.site.register(AnonymousUserDetail)
admin.site.register(StripeDetails)
