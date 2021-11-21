from django.conf.urls import url
from . import views

urlpatterns = [
    # class-period
    url('^class-period/$', views.class_period, name="class_period"),
]
