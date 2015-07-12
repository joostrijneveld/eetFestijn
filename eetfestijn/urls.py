from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^(?i)eetfestijn/admin/', include(admin.site.urls)),
    url(r'^(?i)eetfestijn/', include('orders.urls'))
]
