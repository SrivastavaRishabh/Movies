from django import forms

from .models import Books,Genre,Publisher,Author

class EntryForm(forms.ModelForm):

    class Meta:
        model = Books
        fields = ('name', 'isbn','pages','image','description','genre','publisher','authors','pubdate')