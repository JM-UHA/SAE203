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

class JeuForm(ModelForm):
    class Meta:
        model = models.Jeu
        fields = ("titre", "année de sortie", "photo boite", "éditeur","auteur","catégorie")
        labels = {
            "titre": "Titre",
            "année de sortie": "Annee",
            "photo boite": "Photo",
            "éditeur": "Editeur",
            "auteur": "Auteur",
            "catégorie": "Categorie"
        }
class CategorieForm(ModelForm):
    class Meta:
        model = models.Categorie
        fields = ("nom", "descritif")
        labels = {
            "nom": "Nom",
            "descriptif": "Descriptif",
        }
