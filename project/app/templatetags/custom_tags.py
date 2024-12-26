from django import template
from app.models import SiteSettings, Customer

register = template.Library()

@register.simple_tag
def get_site_logo():
    try:
        settings = SiteSettings.objects.first()
        if settings and settings.logo:
            return settings.logo.url
    except SiteSettings.DoesNotExist:
        return ''
    return ''

@register.simple_tag(takes_context=True)
def profile_pic(context):
    request = context['request']
    try:
        customer = Customer.objects.get(user=request.user)
        if customer.image:
            return customer.image.url
    except Customer.DoesNotExist:
        return ''
    return ''