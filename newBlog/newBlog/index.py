# coding:utf-8
from django.shortcuts import render


def index(request):
    """
    索引页
    :param request:
    :return:
    """
    return render(request, 'blog/index.html')
