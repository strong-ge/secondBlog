from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.post_list, name='post_list'),
    url(r'^detail/(?P<aid>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^time_line/$', views.time_line, name='time_line'),
    url(r'^about/$', views.about, name='about'),
]

