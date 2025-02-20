from django.db import models

from utilisateur.models import CustomUser

# Create your models her
class Projet(models.Model):
    titre = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    def __str__(self):
        return {self.titre}