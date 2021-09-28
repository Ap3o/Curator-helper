from django.conf.urls import url
from . import views

urlpatterns = [
    url('^students/$', views.index, name="get_students")
]
