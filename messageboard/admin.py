from django.contrib import admin

from .models import *
# Register your models here.


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Tags , TagAdmin)
admin.site.register(post)
admin.site.register(Author)
admin.site.register(Comment)
