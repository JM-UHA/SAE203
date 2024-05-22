import typing

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Auteur(models.Model):
    nom = models.CharField(blank=False, max_length=100)
    prenom = models.CharField(blank=False, max_length=100)
    age = models.IntegerField(blank=False)
    photo = models.ImageField(null=True)

    def __str__(self):
        return f"{self.nom} {self.prenom} {self.age}"


class Joueur(models.Model):
    class Type(models.TextChoices):
        particulier = "PAR", "Particulier"
        professionnel = "PRO", "Professionnel"

    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    mail = models.EmailField(max_length=50)
    motdepasse = models.CharField(max_length=50)


class CommentaireJeu(models.Model):
    jeu: models.ForeignKey["models.Model"] = models.ForeignKey(
        "Jeu", on_delete=models.CASCADE
    )  # todo: modifier signature
    joueur: models.ForeignKey["Joueur"] = models.ForeignKey(
        "Joueur", on_delete=models.CASCADE
    )
    note = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    commentaire = models.TextField(max_length=5000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.jeu} noté par {self.joueur} avec {self.note}/10"


MODELS: typing.List[typing.Type[models.Model]] = [Auteur, Joueur, CommentaireJeu]
