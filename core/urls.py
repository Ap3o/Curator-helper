from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # class-period
    url('^$', views.index, name="main"),
    url('^final-performance/$', views.final_performance, name="final_performance"),

    url('^login/$',
        auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name="login"),
    url('^logout/$', views.logout_user, name="logout"),
]
