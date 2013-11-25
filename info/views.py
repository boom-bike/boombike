#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render

def home(request, template='info/home.html'):
    return render(request, template, {})

def test(request, template='info/test.html'):
    return render(request, template, {})

