from django.forms import ModelForm

from . import models


class AuteursForm(ModelForm):
    class Meta:
        model = models.Auteurs
        fields = ("nom", "prenom", "age", "photo")
        labels = {
            "nom": "Nom",
            "prenom": "Prénom",
            "age": "Âge",
            "photo": "Photo",
        }
