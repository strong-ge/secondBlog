from django.contrib import admin

# Register your models here.

from .models import Tag, Blog, Image


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_time', 'update_time',)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'blog', 'top', 'create_time',)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag)
admin.site.register(Image, ImageAdmin)
