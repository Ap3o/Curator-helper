from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name="wrapper"),
    url('^dashboard/$', views.dashboard, name="dashboard"),


    # Academic performance
    url('^academic-performance/$', views.academic_performance, name="academic-performance"),
    url('^academic-performance/get-modal/$', views.academic_performance_modal, name="modal_academic_performance"),
    url('^academic-performance/edit/(?P<pk>\d+)/$', views.academic_performance_edit, name="edit_academic_performance"),
    url('^academic-performance/delete/$', views.academic_performance_delete,
        name="delete_academic_performance"),
    url('^academic-performance/create/$', views.academic_performance_create, name="create_academic_performance"),

    # Student
    url('^students/$', views.student, name="students"),
    url('^students/get-modal/$', views.student_modal, name="modal_students"),
    url('^students/edit/(?P<pk>\d+)/$', views.student_edit, name="edit_students"),
    url('^students/delete/$', views.student_delete,
        name="delete_students"),
    url('^students/create/$', views.student_create, name="create_students"),

    # Teachers
    url('^teachers/$', views.teachers, name="teachers"),
    url('^teachers/get-modal/$', views.teachers_modal, name="modal_teachers"),
    url('^teachers/edit/(?P<pk>\d+)/$', views.teachers_edit, name="edit_teachers"),
    url('^teachers/delete/$', views.teachers_delete,
        name="delete_teachers"),
    url('^teachers/create/$', views.teachers_create, name="create_teachers"),
]
