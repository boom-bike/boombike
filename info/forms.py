#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# Django imports
from django import forms
from django.utils.translation import ugettext as _

# Internal imports
from info.models import CityVisit
from boombike.settings import DATE_INPUT_FORMATS

class VisitedCityForm(forms.ModelForm):
    """
    A form to create a CityVisit with some autocomplete to select a city saved in DB.
    """
#    user = forms.CharField(widget=forms.HiddenInput, required=False)
    location = forms.CharField(widget=forms.TextInput(attrs={'disabled' : ''}),
                               label=_('Location'))
    date = forms.DateField(label=_('Visit date'),
                           widget=forms.TextInput(attrs={'class' : 'datepicker'}),
                           input_formats=DATE_INPUT_FORMATS)

    def save(self, commit=True, user=None):
        # There must be a user
        if user is None:
            return

        location = self.cleaned_data['location']
        date = self.cleaned_data['date']

        instance = CityVisit(location=location, date=date, user=user)

        if commit:
            instance.save()

        return instance

    class Meta:
        model = CityVisit
        exclude = ('user', )
