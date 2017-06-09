from django.conf import settings


def global_settings(request):
    # return any necessary values
    return {
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE,
        'version_number' : settings.VERSION_NUM
    }