from .models import *
# Register your models here.
from django.contrib import admin

class PrepopulateSlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class PrepopulatePeopleSlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('first_name',)}

admin.site.register(PersonType , PrepopulateSlugAdmin)
admin.site.register(Person, PrepopulatePeopleSlugAdmin)
