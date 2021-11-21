from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name="wrapper"),
    url('^dashboard/$', views.dashboard, name="dashboard"),

    # Academic performance
    url('^academic-performance/$', views.academic_performance, name="academic-performance"),

    # Student
    url('^students/$', views.students, name="students"),

    # Teachers
    url('^teachers/$', views.teachers, name="teachers"),

    # Parents
    url('^parents/$', views.parents, name="parents"),

    # Subjects
    url('^subjects/$', views.subjects, name="subjects"),

    # hobbies
    url('^hobbies/$', views.hobbies, name="hobbies"),

    # performance
    url('^performance/$', views.performance, name="performance"),
]
