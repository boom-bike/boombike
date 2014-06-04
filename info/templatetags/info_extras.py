#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# To change this template, choose Tools | Templates
from django.template import Library
from django.core.urlresolvers import resolve, reverse
from django.utils.translation import activate, get_language
from django.template.defaultfilters import stringfilter

register = Library()

@register.simple_tag(takes_context=True)
def change_lang(context, lang=None, *args, **kwargs):
    """
    Get active page's url by a specified language
    Usage: {% change_lang 'en' %}
    """
    path = context['request'].path
    url_parts = resolve(path)

    url = path
    cur_language = get_language()
    try:
        activate(lang)
        url = reverse(url_parts.view_name, kwargs=url_parts.kwargs)
    finally:
        activate(cur_language)

    return "%s" % url


@register.simple_tag(takes_context=True)
def translate_url(context, view_name, *args, **kwargs):
    """
    Get active page's url by a specified language
    Usage: {% translate 'en' %}
    """
    return context['request'].build_absolute_uri(reverse(view_name))


@register.simple_tag
def classname(obj):
    print "Object class:", obj.__class__.__name__
    print "Object dir:", dir(obj)
    print obj
    return True


@register.filter
@stringfilter
def translate_url_filter(url):
    return reverse(url)