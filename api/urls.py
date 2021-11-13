from django.conf.urls import url
from . import views

urlpatterns = [
    url('^students/$', views.index, name="get_students"),
    url('^students/s/$', views.search_for_one_student, name="search_for_one_student"),
    url('^subjects/$', views.get_subjects, name="get_subjects_link"),
    url('^teachers/$', views.get_teachers, name="get_teachers_link"),
    url('^acperf/$', views.get_academic_performance, name="get_academic_performance"),
    # url('^subjects/$', views.get_subjects, name="get_subjects_link"),
]
