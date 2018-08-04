from django import forms
from .models import *


class EntryForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'author', 'body', 'tags', 'status', 'categories',)

