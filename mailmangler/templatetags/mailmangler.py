# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

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

def _encoder(html):
    return b64encode(html.encode('UTF-8')).decode('UTF-8')

def _mailhide(email):
    return mailhide.ashtml(email, PUBLIC, SECRET)

@register.filter
@stringfilter
def mailmangle(email):
    """
    Weakly obfuscates an email address using JavaScript and displays it
    unlinked. If JS not present (i.e. what's in ``<noscript>``), displays
    a link to a reCAPTCHA.
    """
    encoded = _encoder(
        '<span class="email">'
            '{0}'
        '</span>'
        .format(email))

    mh = _mailhide(email)

    return mark_safe(MAIL_PAYLOAD.format(b64enc=encoded, noscript=mh))

@register.filter
@stringfilter
def mailmangle_linked(email):
    """
    Weakly obfuscates an email address using JavaScript and displays it
    with a mailto link. If JS not present (i.e. what's in ``<noscript>``),
    displays a link to a reCAPTCHA.
    """
    encoded = _encoder(
        '<a href="mailto:{0}" class="email">'
            '{0}'
        '</a>'
        .format(email))

    mh = _mailhide(email)
    return mark_safe(MAIL_PAYLOAD.format(b64enc=encoded, noscript=mh))

@register.simple_tag
def mailmangle_js():
    """
    Required to load the decoding script: ``{% load mailmangle_js %}``
    somewhere in the ``<head>``
    """
    return DECODER_SCRIPT
