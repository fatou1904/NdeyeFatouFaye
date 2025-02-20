from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from tache.models import Tache
from utilisateur.models import CustomUser

# Create your views here.

@login_required
def mestache(request):
    # Récupère les tâches créées par l'utilisateur
    taches_creees = Tache.objects.filter(user=request.user)
    
    # Récupère les tâches assignées à l'utilisateur (si c'est un étudiant)
    taches_assignees = Tache.objects.filter(assigned_to=request.user)
    
    return render(request, 'mestache.html', {
        'taches_creees': taches_creees,
        'taches_assignees': taches_assignees
    })
    
    
@login_required
def add_tache(request):
    taches = Tache.objects.all()
    if request.method == "POST":
        titre = request.POST.get('titre')
        description = request.POST.get('description')
        
        # Si c'est un professeur et qu'il veut assigner une tâche
        if request.user.role == 'professeur' and request.POST.get('assigned_to'):
            etudiant = get_object_or_404(CustomUser, id=request.POST.get('assigned_to'))
            Tache.objects.create(
                titre=titre,
                description=description,
                user=request.user,
                assigned_to=etudiant
            )
        else:
            # Création normale de tâche par n'importe quel utilisateur
            Tache.objects.create(
                titre=titre,
                description=description,
                user=request.user
            )
        return redirect('mestache')
    
    # Pour le formulaire, on récupère la liste des étudiants si c'est un professeur
    context = {"taches": taches}
    if request.user.role == 'professeur':
        context['etudiants'] = CustomUser.objects.filter(role='etudiant')
    
    return render(request, 'add_tache.html', context)
    
    




def edit_tache(request, idT):
    tache = get_object_or_404(Tache, id=idT, user=request.user)  # Récupère la tâche en toute sécurité
    if request.method == "POST":
        titre = request.POST.get("titre")
        description = request.POST.get("description")
        tache.titre = titre  # Mets à jour l'attribut titre de la tâche
        tache.description = description  # Mets à jour l'attribut description
        tache.save()  # Sauvegarde les modifications dans la base de données
        return redirect('mestache')  # Redirige vers la liste des tâches
    return render(request, 'edit_tache.html', context={"taches": tache})


def delete_tache(request, idT):
    tache = get_object_or_404(Tache, id=idT, user=request.user)  # Vérifie que la tâche existe
    tache.delete()  # Suppression sécurisée
    return redirect('mestache')  # Assurez-vous que le nom est correct
