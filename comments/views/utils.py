"""
A few bits of helper functions for comment views.
"""

import textwrap
from urllib.parse import urlencode

from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url
from django.core.exceptions import ObjectDoesNotExist

from django_comments.compat import url_has_allowed_host_and_scheme

import django_comments


def next_redirect(request, fallback, **get_kwargs):
    next = request.POST.get('next')
    if not url_has_allowed_host_and_scheme(url=next, allowed_hosts={request.get_host()}):
        next = resolve_url(fallback)

    if get_kwargs:
        if '#' in next:
            tmp = next.rsplit('#', 1)
            next = tmp[0]
            anchor = '#' + tmp[1]
        else:
            anchor = ''

        joiner = ('?' in next) and '&' or '?'
        next += joiner + urlencode(get_kwargs) + anchor
    return HttpResponseRedirect(next)


def confirmation_view(template=''):
    def confirmed(request):
        return render(request, template)

    return confirmed
