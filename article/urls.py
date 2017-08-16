from django.conf.urls import url
from article import views

urlpatterns = [
    url(r'^myview/$', views.myview),
    url(r'^hallo_dunia/$', views.hello_world),
    url(r'^nama/(?P<nama>[\w-]+)/(?P<umur>[0-9]+)$', views.nama_saya),
]