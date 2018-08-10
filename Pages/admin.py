from django.contrib import admin
from .models import Page
# Register your models here.


class PrepSlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Page, PrepSlugAdmin)
