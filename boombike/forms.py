# To change this template, choose Tools | Templates
# and open the template in the editor.

# Django imports
from django import forms

# Internal imports
from info.models import CityVisit, City

class CityVisitForm(forms.ModelForm):
    city = forms.ModelChoiceField(choices=City.objects.none()) # To be interfaced with autocomplete
    date = forms.TextInput(attr={'pickadate' : ''})

    class Meta:
        model = CityVisit
    