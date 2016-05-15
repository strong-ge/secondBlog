from django.contrib import admin

# Register your models here.

from .models import Tag, Blog

admin.site.register(Blog)
admin.site.register(Tag)
