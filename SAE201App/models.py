from django.db import models

class Joueur(models.Model):
    class type (models.TextChoices):
        particulier = "PAR", ("Particulier")
        professionnel = "PRO", ("Professionnel")
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    mail = models.EmailField(max_length=50)
    motdepasse = models.CharField(max_length=50)
    

