from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^update-list/$', views.update_lists, name='update_list'),
]
