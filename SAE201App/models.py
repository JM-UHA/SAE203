import typing

from django.db import models


class Joueur(models.Model):
    class Type(models.TextChoices):
        particulier = "PAR", ("Particulier")
        professionnel = "PRO", ("Professionnel")

    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    mail = models.EmailField(max_length=50)
    motdepasse = models.CharField(max_length=50)


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
