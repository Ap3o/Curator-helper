from django.conf.urls import url
from . import views

urlpatterns = [
    # report
    url('^report/$', views.report, name="report"),

    # EducationalActivities
    url('^educationalactivities/$', views.educationalactivities, name="educationalactivities"),

    # ParentTeacherMeeting
    url('^parentteachermeeting/$', views.parentteachermeeting, name="parentteachermeeting"),
]
