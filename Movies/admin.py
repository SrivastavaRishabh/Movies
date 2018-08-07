from django.contrib import admin
from .models import Movie, Director, Studio, Genre

class PrepopulateSlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Director)
admin.site.register(Studio, PrepopulateSlugAdmin)
admin.site.register(Genre, PrepopulateSlugAdmin)
admin.site.register(Movie, PrepopulateSlugAdmin)