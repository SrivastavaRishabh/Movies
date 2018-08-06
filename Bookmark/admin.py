from django.contrib import admin
from .models import Bookmarks


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'description')

admin.site.register(Bookmarks,BookmarkAdmin)