from django.conf.urls import url
from . import views

urlpatterns = [
    # performance
    url('^report/$', views.report, name="report"),
    url('^report/get-modal/$', views.report_modal, name="modal_report"),
    url('^report/edit/(?P<pk>\d+)/$', views.report_edit, name="edit_report"),
    url('^report/delete/$', views.report_delete,
        name="delete_report"),
    url('^report/create/$', views.report_create, name="create_report"),
]
