#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# Django imports
from django.utils.translation import ugettext as _

# External imports
import django_tables2 as tables
from django_tables2.utils import A

# Internal imports
from info.models import CityVisit

class CityVisitTable(tables.Table):
    location = tables.Column(verbose_name=_('Checkpoint'))
    date = tables.Column(verbose_name=_('Date'))

    class Meta:
        model = CityVisit
        exclude = ('id', 'user')
        attrs = {"class": "paleblue"}
        order_by = ('date', )

class GroupedCityVisitTable(tables.Table):
    location = tables.LinkColumn('city_visit', args=[A('location')], verbose_name=_('Location'))
    num_visits = tables.Column(verbose_name=_('# Stops in location'))

    class Meta:
        attrs = {'class': 'paleblue'}
        order_by = ('-num_visits', )