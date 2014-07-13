#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# Python imports
import json

# Django imports
from info.models import CityVisit
from django.shortcuts import render, render_to_response
from django.utils.translation import ugettext as _
from django_tables2   import RequestConfig
from django.db.models import Count
from django.contrib.auth.models import User

# Internal imports
from info.forms import VisitedCityForm
from info.tables import CityVisitTable, GroupedCityVisitTable
from boombike.settings import GOOGLE_MAPS_API_KEY

def home(request, template='info/home.html'):
    return render(request, template, {})

def bicycle_touring(request, template='info/bicycle_touring.html'):
    return render(request, template, {})

def boom_festival(request, template='info/boom_festival.html'):
    return render(request, template, {})

def boom_and_bike(request, template='info/boom_and_bike.html'):
    return render(request, template, {})

def get_there(request, template='info/get_there.html'):
    return render(request, template, {})

def together(request, template='info/together.html'):
    context_dict = {}

    if request.method == 'GET':
        form = VisitedCityForm()
        context_dict['form'] = form

    elif request.method == 'POST':
        form = VisitedCityForm(request.POST)
        context_dict['form'] = form

        if form.is_valid(): # All validation rules pass
           city_visit = form.save(user=request.user) # Do not let the user change this by any mean :)
           message = u'%s "%s"' % (unicode(_("You successfully added a checkpoint at")), city_visit.location)
           context_dict['form'] = VisitedCityForm() # We want the form to blank here
        else:
            message = _('Something bad happened...')
            print form.errors

        context_dict['message'] = message

    if request.user.is_authenticated():
        user_city_visits = CityVisit.objects.filter(user=request.user)
        city_visits_table = CityVisitTable(user_city_visits, prefix='user')
        RequestConfig(request, paginate={"per_page": 10}).configure(city_visits_table)

        context_dict['nb_city_visits'] = user_city_visits.count()
        context_dict['city_visits_table'] = city_visits_table

    # Anyway, we get all the users city visits
    all_users_city_visits = CityVisit.objects.all().values('location').annotate(num_visits=Count('location'))
    all_users_city_visits_table = GroupedCityVisitTable(all_users_city_visits, prefix='all_users')
    RequestConfig(request, paginate={"per_page": 15}).configure(all_users_city_visits_table)
    context_dict['all_users_city_visits_table'] = all_users_city_visits_table
    context_dict['all_users_city_visits_count'] = len(all_users_city_visits)

    # Finally, we need the right API Key
    context_dict['GOOGLE_MAPS_API_KEY'] = GOOGLE_MAPS_API_KEY

    return render(request, template, context_dict)


def city_visit(request, location, template='info/city_visit.html'):
    context_dict = {}

    # Who are the users visiting the city?
    users_visiting = CityVisit.objects.filter(location=location)\
                        .order_by('user').values_list('user', flat=True).distinct()

    users = User.objects.filter(pk__in=users_visiting)
    context_dict['users'] = users
    context_dict['location'] = location

    return render(request, template, context_dict)


def user_checkpoints(request, id, template='info/user_checkpoints.html'):
    context_dict = {}

    # Get the user
    user = User.objects.get(pk=id)

    # Get the user's checkoints
    user_checkpoints = CityVisit.objects.filter(user=user)

    # Build the table
    user_checkpoints_table = CityVisitTable(user_checkpoints, prefix='user')
    RequestConfig(request, paginate={"per_page": 15}).configure(user_checkpoints_table)
    context_dict['user_checkpoints_table'] = user_checkpoints_table

    context_dict['username'] = user.username

    user_unique_checkpoints = user_checkpoints.order_by('location')\
        .values_list('location', flat=True).distinct()

    context_dict['user_unique_checkpoints'] = json.dumps(list(user_unique_checkpoints))
    context_dict['current_user'] = user

    context_dict['language_code'] = request.LANGUAGE_CODE

    return render(request, template, context_dict)


def page_not_found(request, template='404.html'):
    response = render(request, template)
    response.status_code = 404
    return response

def albums(request, template='music/albums.html'):
    return render_to_response(template)
