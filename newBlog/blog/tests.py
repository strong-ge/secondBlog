from django.test import TestCase
from blog.models import Blog


class SimpleTest(TestCase):
    def listall(self):
        blogs = Blog.objects.order_by('-update_time')
        print blogs
