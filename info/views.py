#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response
#from django.utils.translation import ugettext as _

def home(request, template='info/home.html'):
    return render(request, template, {})

def bicycle_touring(request, template='info/bicycle_touring.html'):
    return render(request, template, {})

def boom_festival(request, template='info/boom_festival.html'):
    return render(request, template, {})

def boom_and_bike(request, template='info/boom_and_bike.html'):
    return render(request, template, {})

def page_not_found(request, template='404.html'):
    response = render(request, template)
    response.status_code = 404
    return response

def albums(request, template='music/albums.html'):
    return render_to_response(template)
