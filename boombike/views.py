#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render

def handler_404_page(request, template='404.html'):
    response = render(request, template)
    response.status_code = 404
    return response
