from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from tache.models import Tache 
from .form import CustomUserCreationForm, ProfileForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('connexion')
    else:
        form = CustomUserCreationForm()
    return render(request, 'inscription.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'connexion.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

def deconnexion(request):
    logout(request)
    return redirect('connexion')

def accueil(request):
    return render(request, 'accueil')

@login_required
def editerProfile(request):
    user = request.user  # Récupère l'utilisateur connecté

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=user)
       
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirige vers la page du profil après mise à jour
    else:
        form = ProfileForm(instance=user)  # Pré-rempli avec les données actuelles

    context = {'form': form}
    return render(request, 'profile_form.html', context)

@login_required
def changer_mot_de_passe(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)  # Modifié l'ordre des arguments
        if form.is_valid():
            user = form.save()  # Sauvegarde et récupère l'utilisateur
            update_session_auth_hash(request, user)  # Utilise l'utilisateur mis à jour
            messages.success(request, "Votre mot de passe a été mis à jour avec succès.")
            return redirect('profile')
        else:
            for error in form.errors.values():
                messages.error(request, error)  # Affiche les erreurs spécifiques
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'changer_mot_de_passe.html', {'form': form})