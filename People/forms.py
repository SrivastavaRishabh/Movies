from django import forms
from .models import *


class EntryForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ('first_name','last_name','gender','image','birth_date','person_types','website',)

