from django.db import models

from utilisateur.models import CustomUser

# Create your models here.
class Tache(models.Model):
    titre = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='taches_creees')
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name='taches_assignees')
    
    def __str__(self):
        return self.titre