from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^(?P<trip_id>\d+)/$', views.index, name='index')
]   

