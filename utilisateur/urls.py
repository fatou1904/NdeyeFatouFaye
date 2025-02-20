
from django import views
from django.contrib import admin
from django.urls import  path, include
from django.conf.urls.static import static
from monprojet import settings
from utilisateur.views import accueil, changer_mot_de_passe, editerProfile, profile, connexion, inscription, deconnexion

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('', inscription, name='inscription'),
    path('connexion/', connexion, name='connexion'),
    path('accueil/', accueil, name='accueil'),
    path('edit/', editerProfile, name='editerProfile'),
    path('deconnexion/', deconnexion, name='deconnexion'),
    path('changerpwd/', changer_mot_de_passe, name='changerpwd'),
    path('', include('project.urls')),
    path('', include('tache.urls')),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
