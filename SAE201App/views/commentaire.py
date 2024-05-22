from django.http import HttpRequest
from django.shortcuts import render

from ..forms import CommentaireForm
from ..models import CommentaireJeu


def commentaire_all(request: HttpRequest, jeu_id: int):
    """Retourne tout les commentaires."""
    # try:
    #     jeu = Jeu.objects.get(id=jeu_id)
    # except Jeu.DoesNotExist:
    #     return render(request, "jeux/not_found.html", {"id": jeu_id})

    # commentaires = CommentaireJeu.objects.filter(jeu=jeu)
    commentaires = CommentaireJeu.objects.filter()
    return render(request, "commentaires/all.html", {"commentaires": commentaires})


def commentaire_create(request: HttpRequest, jeu_id: int):
    """Ajoute un commentaire."""
    # try:
    #     jeu = Jeu.objects.get(id=jeu_id)
    # except Jeu.DoesNotExist:
    #     return render(request, "jeux/not_found.html", {"id": jeu_id})

    if request.method == "GET":
        return render(request, "commentaires/add.html", {"form": CommentaireForm()})

    if request.method == "POST":
        form = CommentaireForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, "commentaires/add.html", {"form": form})

    return commentaire_all(request, jeu_id)


def commentaire_view(request: HttpRequest, jeu_id: int, id: int):
    """Retourne un commentaire."""
    # try:
    #     jeu = Jeu.objects.get(id=jeu_id)
    # except Jeu.DoesNotExist:
    #     return render(request, "jeux/not_found.html", {"id": jeu_id})

    try:
        commentaire = CommentaireJeu.objects.get(id=id)
    except CommentaireJeu.DoesNotExist:
        return render(request, "commentaires/not_found.html", {"id": id})
    return render(request, "commentaires/view.html", {"commentaire": commentaire})


def commentaire_edit(request: HttpRequest, jeu_id: int, id: int):
    """Modifie un commentaire."""
    # try:
    #     jeu = Jeu.objects.get(id=jeu_id)
    # except Jeu.DoesNotExist:
    #     return render(request, "jeux/not_found.html", {"id": jeu_id})

    try:
        commentaire = CommentaireJeu.objects.get(id=id)
    except CommentaireJeu.DoesNotExist:
        return render(request, "commentaires/not_found.html", {"id": id})

    if request.method == "GET":
        return render(
            request,
            "commentaires/edit.html",
            {"form": CommentaireForm(), "jeu": jeu, "commentaire": commentaire},
        )
    if request.method == "POST":
        form = CommentaireForm(request.POST, instance=commentaire)
        if form.is_valid():
            form.save()
        else:
            return render(request, "commentaires/edit.html", {"form": form})
    return commentaire_view(request, jeu_id, id)


def commentaire_delete(request: HttpRequest, jeu_id: int, id: int):
    """Supprime un commentaire."""
    # try:
    #     jeu = Jeu.objects.get(id=jeu_id)
    # except Jeu.DoesNotExist:
    #     return render(request, "jeux/not_found.html", {"id": jeu_id})

    try:
        commentaire = CommentaireJeu.objects.get(id=id)
    except CommentaireJeu.DoesNotExist:
        return render(request, "commentaires/not_found.html", {"id": id})

    commentaire.delete()
    return commentaire_all(request, jeu_id)
