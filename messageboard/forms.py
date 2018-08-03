from django import forms
from .models import *


class EntryForm(forms.ModelForm):

    class Meta:
        model = post
        fields = ('title', 'content', 'tag', 'author')