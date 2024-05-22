from django.forms import ModelForm

from . import models


class JoueurForm(ModelForm):
    class Meta:
        model = models.Joueur
        fields = ("nom", "prenom", "mail", "type")
