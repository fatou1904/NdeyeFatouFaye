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
from project.views import add_projet, delete_projet, mesprojets


urlpatterns = [
   
    path('mesprojets/', mesprojets, name='mesprojets'),
    path('add_projet/', add_projet, name='add_projet'),
    path('delete-projet/<int:idP>', delete_projet, name='delete_projet'),
    path('', include('tache.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)