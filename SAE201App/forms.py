from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
class JoueurForm(ModelForm):
    class Meta:
        model = models.Joueur
        fields = ('nom','prenom','mail','type')