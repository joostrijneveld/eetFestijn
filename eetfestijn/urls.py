from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^(?i)eetfestijn/admin/', include(admin.site.urls)),
    url(r'^(?i)eetfestijn/', include('orders.urls', namespace='orders'))
)
