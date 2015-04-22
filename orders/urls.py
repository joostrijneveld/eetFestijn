from django.conf.urls import patterns, url
from orders import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^summary/$', views.summary, name='summary'),
    url(r'^summary\.pdf$', views.summary_PDF, name='summary_PDF'),
    url(r'^overview/$', views.overview, name='overview'),
]
