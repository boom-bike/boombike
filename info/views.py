#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render
#from django.utils.translation import ugettext as _

def home(request, template='info/home.html'):
    return render(request, template, {})

def home_details(request, template='info/home_details.html'):
    return render(request, template, {})

def bicycle_touring(request, template='info/bicycle_touring.html'):
    return render(request, template, {})

def boom_festival(request, template='info/boom_festival.html'):
    return render(request, template, {})

def boom_and_bike(request, template='info/boom_and_bike.html'):
    return render(request, template, {})

