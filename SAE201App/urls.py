from django.urls import path

from .views import commentaire

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
]
