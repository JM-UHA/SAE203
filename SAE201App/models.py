import typing

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Auteur(models.Model):
    nom = models.CharField(blank=False, max_length=100)
    prenom = models.CharField(blank=False, max_length=100)
    age = models.IntegerField(blank=False)
    photo = models.ImageField(null=True)

    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.age}"


class Joueur(models.Model):
    class Type(models.TextChoices):
        particulier = "PAR", "Particulier"
        professionnel = "PRO", "Professionnel"

    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    mail = models.EmailField(max_length=254)
    motdepasse = models.CharField(max_length=50)
    type = models.CharField(max_length=3, choices=Type)  # type: ignore

    def __str__(self) -> str:
        return f"{self.nom} {self.prenom} - {self.mail}"


class CommentaireJeu(models.Model):
    jeu: models.ForeignKey["Jeu"] = models.ForeignKey("Jeu", on_delete=models.CASCADE)
    joueur: models.ForeignKey["Joueur"] = models.ForeignKey(
        "Joueur", on_delete=models.CASCADE
    )
    note = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    commentaire = models.TextField(max_length=5000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.jeu} - {self.joueur} avec {self.note}/10"


class Jeu(models.Model):

    titre = models.CharField(max_length=100)
    annee = models.IntegerField()
    editeur = models.CharField(max_length=100)
    auteur = models.ForeignKey("Auteur", on_delete=models.CASCADE)
    categorie = models.ForeignKey("CategorieJeu", on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(null=True)

    def __str__(self) -> str:
        return f"{self.titre} - {self.editeur} - {self.annee}"


class CategorieJeu(models.Model):

    nom = models.CharField(max_length=50)
    descriptif = models.TextField(max_length=5000)

    def __str__(self) -> str:
        return f"{self.nom}"


MODELS: typing.List[typing.Type[models.Model]] = [
    Auteur,
    Joueur,
    Jeu,
    CommentaireJeu,
    CategorieJeu,
]
