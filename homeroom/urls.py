from django.conf.urls import url
from . import views

urlpatterns = [
    # class-period
    url('^class-period/$', views.class_period, name="class_period"),
    # spent-class-period
    url('^spent-class-period/$', views.spent_class_period, name="spent_class_period"),
]
