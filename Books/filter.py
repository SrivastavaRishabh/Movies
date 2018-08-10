import django_filters
from .models import Books


class BookFilter(django_filters.FilterSet):

    class Meta:
            model = Books
            fields = ['genre', 'publisher', 'authors']
