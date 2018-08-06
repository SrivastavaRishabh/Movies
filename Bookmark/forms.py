from django.forms import ModelForm
from .models import Bookmarks

class BookmarksForm(ModelForm):
    class Meta:
        model = Bookmarks
        fields=['name','url','description','tags']