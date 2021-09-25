from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name=""),
    url('^dashboard/$', views.dashboard, name="")
]
