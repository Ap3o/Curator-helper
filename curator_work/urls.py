from django.conf.urls import url
from . import views

urlpatterns = [
    # report
    url('^report/$', views.report, name="report"),
    url('^report/get-modal/$', views.report_modal, name="modal_report"),
    url('^report/edit/(?P<pk>\d+)/$', views.report_edit, name="edit_report"),
    url('^report/delete/$', views.report_delete,
        name="delete_report"),
    url('^report/create/$', views.report_create, name="create_report"),

    # EducationalActivities
    url('^educationalactivities/$', views.educationalactivities, name="educationalactivities"),
    url('^educationalactivities/get-modal/$', views.educationalactivities_modal, name="modal_educationalactivities"),
    url('^educationalactivities/edit/(?P<pk>\d+)/$', views.educationalactivities_edit, name="edit_educationalactivities"),
    url('^educationalactivities/delete/$', views.educationalactivities_delete,
        name="delete_educationalactivities"),
    url('^educationalactivities/create/$', views.educationalactivities_create, name="create_educationalactivities"),
]
