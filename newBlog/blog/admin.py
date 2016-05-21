from django.contrib import admin

# Register your models here.

from .models import Tag, Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_time', 'update_time',)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag)
