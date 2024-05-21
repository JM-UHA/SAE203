from django.db import models
from django.db import models

class Auteurs(models.Model):
    nom = models.CharField(blank =False, max_length=100)
    prenom = models.CharField(blank=False, max_length=100)
    age = models.IntegerField(blank=False)
    photo= models.ImageField(null = True)
def __str__(self):
    chaine = f"{self.nom} {self.prenom} {self.age} {self.photo}"

# Create your models here.
