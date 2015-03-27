from django.conf.urls import patterns, url
from orders import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^summary/$', views.summary, name='summary'),
    url(r'^overview/$', views.overview, name='overview'),
)