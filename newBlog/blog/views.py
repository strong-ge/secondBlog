from django.shortcuts import render
from blog.models import Tag, Blog, Image
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from function import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from blog.serializers import BlogSerializer
from django.http import HttpResponse


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json;charset=UTF-8'
        super(JSONResponse, self).__init__(content, **kwargs)


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
    image = blog.images.all()
    return render(request, 'blog/test.html', {'blog': blog, 'image': image})


@csrf_exempt
def blog_list_api(request):
    """
    List all code blogs, or create a new blog.
    """
    if request.method == 'GET':
        snippets = Blog.objects.all()
        serializer = BlogSerializer(snippets, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BlogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def blog_detail_api(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BlogSerializer(blog)
        return JSONResponse(serializer.data)