from django.conf.urls import url
from . import views

urlpatterns = [
    # class-period
    url('^$', views.index, name="main"),
    url('^final-performance/$', views.final_performance, name="final_performance"),
]
