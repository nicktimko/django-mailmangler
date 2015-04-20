# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from base64 import b64encode

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from django.templatetags.static import static
from recaptcha.client import mailhide

from ..settings import PUBLIC, SECRET

register = template.Library()

MAIL_PAYLOAD = (
    '<script type="text/javascript">'
        'document.write(Base64.decode("{b64enc}"));'
    '</script>'
    '<noscript>'
        '{noscript}'
    '</noscript>'
)

# TODO: use format_html instead of mark_safe:
# https://docs.djangoproject.com/en/1.8/ref/utils/#django.utils.html.format_html
DECODER_SCRIPT = mark_safe(
    '<script type="text/javascript" src="{0}"></script>'.format(static(
        'mailmangler/js/base64.min.js')))

@register.filter
@stringfilter
def mailmangle(email):
    span = '<span class="email">{0}</span>'.format(email)
    encoded = b64encode(span)
    mh = mailhide.ashtml(email, PUBLIC, SECRET)
    return mark_safe(JS_DECODER.format(b64enc=encoded, noscript=mh))

@register.filter
@stringfilter
def mailmangle_linked(email):
    link = '<a href="mailto:{0}" class="email">{0}</a>'.format(email)
    encoded = b64encode(link)
    mh = mailhide.ashtml(email, PUBLIC, SECRET)
    return mark_safe(JS_DECODER.format(b64enc=encoded, noscript=mh))

@register.simple_tag
def mailmangle_js():
    return DECODER_SCRIPT
