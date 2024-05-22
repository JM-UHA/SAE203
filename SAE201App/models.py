import typing

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


class CommentaireJeux(models.Model):
    jeux: models.ForeignKey["models.Model"] = models.ForeignKey(
        "Jeux", on_delete=models.CASCADE
    )  # todo: modifier signature
    joueurs: models.ForeignKey["models.Model"] = models.ForeignKey(
        "Joueurs", on_delete=models.SET_NULL
    )  # todo: modifier signature
    note = models.IntegerField()
    commentaire = models.TextField(max_length=5000)
    date = models.DateTimeField(auto_now_add=True)


MODELS: typing.List[typing.Type[models.Model]] = [CommentaireJeux]
