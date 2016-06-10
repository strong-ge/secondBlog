# coding:utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/$', views.post_list, name='post_list'),
    url(r'^detail/(?P<aid>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^time_line/$', views.time_line, name='time_line'),
    url(r'^about/$', views.about, name='about'),
    url(r'^test/$', views.test, name='test'),

    url(r'^api/$', views.blog_list_api),  # 序列化博客列表
    url(r'^api/(?P<pk>[0-9]+)/$', views.blog_detail_api),  # 序列化博客详情
]
