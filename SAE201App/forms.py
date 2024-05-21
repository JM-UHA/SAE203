from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class AuteursForm(ModelForm):
    class Meta:
        model = models.Auteurs
        fields = ('nom' , 'prenom', 'age' , 'photo')
        labels = {
            'nom' : _('Nom'),
            'prenom': _('Prénom'),
            'age': _('Âge'),
            'photo': _('photo'),
        }
