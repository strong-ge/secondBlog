from django.shortcuts import render
from blog.models import Tag, Blog
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from function import *
# from django.http import HttpResponse


def index(request):
    return render(request, 'blog/index.html')


def post_list(request):
    blogs = Blog.objects.order_by('-publish_time')
    paginator = Paginator(blogs, 8)
    page = request.GET.get('page')
    try:
        blog_list = paginator.page(page)
    except PageNotAnInteger:
        blog_list = paginator.page(1)
    except EmptyPage:
        blog_list = paginator.paginator(paginator.num_pages)
    return render(request, 'blog/list.html', {'blog_list': blog_list})


def post_detail(request, aid):
    blog = Blog.objects.get(id=int(aid))
    return render(request, 'blog/detail.html', {'blog': blog})


def time_line(request):
    date_list = get_blog_by_month()
    return render(request, 'blog/time_line.html', {'date_list': date_list})


def about(request):
    #   TODO
    return render(request, 'blog/about.html')


def test(request):
    blog = Blog.objects.get(id=1)
    return render(request, 'blog/test.html', {'blog': blog})
