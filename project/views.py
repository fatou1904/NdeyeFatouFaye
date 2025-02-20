from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from project.models import Projet

# Create your views here.

def mesprojets(request):
    projets = Projet.objects.filter(user=request.user)
    return render(request, 'mesprojets.html', {'project': projets})

@login_required
def add_projet(request):
    projets = Projet.objects.all()
    if request.method=="POST":
        titre = request.POST.get('titre')
        description = request.POST.get('description')
        Projet.objects.create(
            titre = titre,
            description = description,
            user = request.user
        )
       
        return redirect('mesprojets')
    return render (request, 'add_projet.html', {"project":projets})

def delete_projet(request, idP):
    projets = get_object_or_404(Projet, id=idP, user=request.user)  # Vérifie que la tâche existe
    projets.delete()  # Suppression sécurisée
    return redirect('mesprojets')  # Assurez-vous que le nom est correct
