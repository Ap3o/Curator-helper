from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name="wrapper"),
    url('^dashboard/$', views.dashboard, name="dashboard"),
    url('^academic-performance/$', views.academic_performance, name="tables"),

    url('^academic-performance/get-modal/$', views.academic_performance_modal, name="modal_academic_performance"),
    url('^academic-performance/edit/(?P<pk>\d+)/$', views.academic_performance_edit, name="edit_academic_performance"),
    url('^academic-performance/delete/$', views.academic_performance_delete,
        name="delete_academic_performance"),
    url('^academic-performance/create/$', views.academic_performance_create, name="create_academic_performance")
]
