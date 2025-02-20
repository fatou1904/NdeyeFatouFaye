from django.contrib.auth.models import AbstractUser, Permission
from django.db import models
from django.contrib.contenttypes.models import ContentType

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100)  
    last_name = models.CharField(max_length=100)  
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    datecreation = models.DateTimeField(auto_now_add=True)

    ETUDIANT = 'etudiant'
    PROFESSEUR = 'professeur'
    CHOIX_ROLE = [(ETUDIANT, "Étudiant"), (PROFESSEUR, "Professeur")]
    role = models.CharField(max_length=10, choices=CHOIX_ROLE, default=ETUDIANT)

    def __str__(self):
        return self.username
