from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name="wrapper"),
    url('^dashboard/$', views.dashboard, name="dashboard")
]
