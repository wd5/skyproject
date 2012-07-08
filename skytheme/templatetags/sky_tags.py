from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe


register = template.Library()


def urlize_ext(value, nofollow=False, autoescape=None):
    """Converts URLs in plain text into clickable links."""
    from django.utils.html import urlize
    return mark_safe(urlize(value, nofollow=nofollow, autoescape=autoescape))
urlize_ext.is_safe=True
urlize_ext.needs_autoescape = True
urlize_ext = stringfilter(urlize_ext)


register.filter(urlize_ext)
