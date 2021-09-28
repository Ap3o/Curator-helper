from django.conf.urls import url
from . import views

urlpatterns = [
    url('^students/$', views.index, name="get_students"),
    url('^students/s/$', views.search_for_one_student, name="search_for_one_student")
]
