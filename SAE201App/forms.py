from django.forms import ModelForm

from . import models


class AuteursForm(ModelForm):
    class Meta:
        model = models.Auteur
        fields = ("nom", "prenom", "age", "photo")
        labels = {
            "nom": "Nom",
            "prenom": "Prénom",
            "age": "Âge",
            "photo": "Photo",
        }


class JoueurForm(ModelForm):
    class Meta:
        model = models.Joueur
        fields = ("nom", "prenom", "mail", "type")
        labels = {
            "nom": "Nom",
            "prenom": "Prénom",
            "mail": "Mail",
            "type": "Type",
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
