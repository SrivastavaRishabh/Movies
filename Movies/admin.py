from django.contrib import admin
from .models import *
# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Genre, GenreAdmin)


class StudioAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Studio, StudioAdmin)


admin.site.register(Director)


class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Movie, MovieAdmin)