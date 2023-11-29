from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ABOUT/', views.ABOUT),
    path('CONTACT/', views.CONTACT),
    path('GALLARY/', views.GALLARY),
    path('', views.HOME),
    path('SERVICE/', views.SERVICE),
    path('UPDATE/', views.UPDATE),
 
]

if settings.DEBUG:
    urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    