from django import forms
from django.forms import ModelForm

from . import models


class AuteurForm(ModelForm):
    class Meta:
        model = models.Auteur
        fields = ("nom", "prenom", "age", "photo")
        labels = {
            "nom": "Nom",
            "prenom": "Prénom",
            "age": "Âge",
            "photo": "Photo",
        }


class CategorieForm(ModelForm):
    class Meta:
        model = models.CategorieJeu
        fields = ("nom", "descriptif")
        labels = {
            "nom": "Nom",
            "descriptif": "Descriptif",
        }


class CommentaireForm(ModelForm):
    class Meta:
        model = models.CommentaireJeu
        fields = ("jeu", "joueur", "note", "commentaire")
        labels = {
            "jeu": "Jeu",
            "joueur": "Joueur",
            "note": "Votre note sur 10",
            "commentaire": "Commentaire",
        }


class JeuForm(ModelForm):
    class Meta:
        model = models.Jeu
        fields = ("titre", "annee", "photo", "editeur", "auteur", "categorie")
        labels = {
            "titre": "Titre",
            "annee": "Année",
            "photo": "Photo",
            "editeur": "Éditeur",
            "auteur": "Auteur",
            "categorie": "Catégorie",
        }


class JoueurForm(ModelForm):
    class Meta:
        model = models.Joueur
        fields = ("nom", "prenom", "motdepasse", "mail", "type")
        labels = {
            "nom": "Nom",
            "prenom": "Prénom",
            "motdepasse": "Mot de passe",
            "mail": "Mail",
            "type": "Type",
        }


class ImportJeu(forms.Form):
    fichier = forms.FileField()
