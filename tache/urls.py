"""
URL configuration for monprojet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path

from monprojet import settings
from tache.views import add_tache, delete_tache, edit_tache, mestache



urlpatterns = [
   
    path('mestache/', mestache, name='mestache'),
    path('add_tache/', add_tache, name='add_tache'),
    path('edit_tache/<int:idT>', edit_tache, name='edit_tache'),
    path('delete/<int:idT>', delete_tache, name='delete_tache'),

   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)