from django.urls import path

from .views import commentaire
from .views import categorie
from .views import jeu
from .views import joueur

urlpatterns = [
    path("commentaire/<int:jeu_id>/", commentaire.all, name="commentaire.all"),
    path(
        "commentaire/<int:jeu_id>/create/",
        commentaire.create,
        name="commentaire.create",
    ),
    path(
        "commentaire/<int:jeu_id>/<int:id>/", commentaire.view, name="commentaire.view"
    ),
    path(
        "commentaire/<int:jeu_id>/<int:id>/edit/",
        commentaire.edit,
        name="commentaire.edit",
    ),
    path(
        "commentaire/<int:jeu_id>/<int:id>/delete/",
        commentaire.delete,
        name="commentaire.delete",
    ),

    path("categorie/<int:id>/", categorie.all, name="categorie.all"),
    path(
        "categorie/<int:id>/create/",
        categorie.create,
        name="categorie.create",
    ),
    path(
        "categorie/<int:id>/", categorie.view, name="categorie.view"
    ),
    path(
        "categorie/<int:id>/edit/",
        categorie.edit,
        name="categorie.edit",
    ),
    path(
        "categorie/<int:id>/delete/",
        categorie.delete,
        name="categorie.delete",
    ),

    path("jeu/<int:id>/", jeu.all, name="jeu.all"),
    path(
        "jeu/<int:id>/create/",
        jeu.create,
        name="jeu.create",
    ),
    path(
        "jeu/<int:id>/", jeu.view, name="jeu.view"
    ),
    path(
        "jeu/<int:id>/edit/",
        jeu.edit,
        name="jeu.edit",
    ),
    path(
        "jeu/<int:id>/delete/",
        jeu.delete,
        name="jeu.delete",
    ),

    path("joueur/<int:id>/", joueur.all, name="joueur.all"),
    path(
        "joueur/<int:id>/create/",
        joueur.create,
        name="joueur.create",
    ),
    path(
        "joueur/<int:id>/", joueur.view, name="joueur.view"
    ),
    path(
        "joueur/<int:id>/edit/",
        joueur.edit,
        name="joueur.edit",
    ),
    path(
        "joueur/<int:id>/delete/",
        joueur.delete,
        name="joueur.delete",
    ),
]
