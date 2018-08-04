from .models import *
# Register your models here.
from django.contrib import admin

class PrepopulateSlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category , PrepopulateSlugAdmin)
admin.site.register(Post, PrepopulateSlugAdmin)
admin.site.register(Author)
