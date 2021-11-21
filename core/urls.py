from django.conf.urls import url
from . import views

urlpatterns = [
    # class-period
    url('^$', views.index, name="main"),
    url('^dashboard/$', views.dashboard, name="dashboard"),
]
