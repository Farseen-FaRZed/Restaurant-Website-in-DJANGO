from django.conf import settings


def site_settings(request):
    """
    Makes the SITE_CONFIG dict from settings.py available in every
    template as {{ site }}. That's it - that's the whole file.
    """
    return {'site': settings.SITE_CONFIG}
