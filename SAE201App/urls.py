from django.urls import path

from SAE201App.views import auteurs

from .views import categorie, commentaire, jeu, joueur, ludotheque

urlpatterns = [
    path("", ludotheque, name="ludotheque"),
    # Auteurs
    path("auteurs/", auteurs.all, name="auteur.all"),
    path("auteurs/create/", auteurs.create, name="auteur.create"),
    path("auteurs/<int:id>/", auteurs.view, name="auteur.view"),
    path("auteurs/<int:id>/edit/", auteurs.edit, name="auteur.edit"),
    path("auteurs/<int:id>/delete/", auteurs.delete, name="auteur.delete"),
    # Categorie
    path("categorie/", categorie.all, name="categorie.all"),
    path(
        "categorie/create/",
        categorie.create,
        name="categorie.create",
    ),
    path("categorie/<int:id>/", categorie.view, name="categorie.view"),
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
    # Commentaires
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
    # Jeux
    path("jeu/", jeu.all, name="jeu.all"),
    path(
        "jeu/create/",
        jeu.create,
        name="jeu.create",
    ),
    path("jeu/<int:id>/", jeu.view, name="jeu.view"),
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
    path(
        "jeu/import/",
        jeu.import_jeu,
        name="jeu.import",
    ),
    # Joueurs
    path("joueur/", joueur.all, name="joueur.all"),
    path(
        "joueur/create/",
        joueur.create,
        name="joueur.create",
    ),
    path("joueur/<int:id>/", joueur.view, name="joueur.view"),
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
    path(
        "joueur/<int:id>/commentaire/",
        joueur.commentaire,
        name="joueur.commentaire",
    ),
]
