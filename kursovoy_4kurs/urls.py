from django.contrib import admin
from django.urls import path, include

handler404 = 'core.views.handler404'
handler500 = 'core.views.handler500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('education/', include('education.urls')),
    path('curator_work/', include('curator_work.urls')),
    path('homeroom/', include('homeroom.urls')),
    path('api/', include('api.urls')),
    path('', include('core.urls')),
    path("select2/", include("django_select2.urls")),
]
