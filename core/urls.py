from django.conf.urls import url

from . import views

app_name = "core"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^facture/$', views.facture, name='facture'),
    url(r'^user/$', views.client, name='client'),
]
