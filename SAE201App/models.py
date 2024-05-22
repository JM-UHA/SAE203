import typing

from django.db import models

# Create your models here.


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
