from django.contrib import admin
from .models import Books, Genre, Publisher, Author
# Register your models here.

admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Books)
