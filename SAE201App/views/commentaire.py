from django.http import HttpRequest
from django.shortcuts import render

from ..forms import CommentaireNoJeuForm, CommentaireNoJoueurForm
from ..models import CommentaireJeu, Jeu


def all(request: HttpRequest, jeu_id: int):
    """Retourne tout les commentaires."""
    try:
        jeu = Jeu.objects.get(id=jeu_id)
    except Jeu.DoesNotExist:
        return render(request, "jeux/not_found.html", {"id": jeu_id})

    commentaires = CommentaireJeu.objects.filter(jeu=jeu)

    return render(
        request, "commentaires/all.html", {"commentaires": commentaires, "jeu": jeu}
    )


def create(request: HttpRequest, jeu_id: int):
    """Ajoute un commentaire."""
    try:
        jeu = Jeu.objects.get(id=jeu_id)
    except Jeu.DoesNotExist:
        return render(request, "jeux/not_found.html", {"id": jeu_id})

    if request.method == "GET":
        return render(
            request,
            "commentaires/create.html",
            {"form": CommentaireNoJeuForm(), "jeu": jeu},
        )

    if request.method == "POST":
        form = CommentaireNoJeuForm(request.POST)
        if form.is_valid():
            commentaire: CommentaireJeu = form.save(commit=False)
            commentaire.jeu = jeu
            commentaire.save()
        else:
            return render(
                request, "commentaires/create.html", {"form": form, "jeu": jeu}
            )

    return all(request, jeu_id)


def view(request: HttpRequest, jeu_id: int, id: int):
    """Retourne un commentaire."""
    try:
        jeu = Jeu.objects.get(id=jeu_id)
    except Jeu.DoesNotExist:
        return render(request, "jeux/not_found.html", {"id": jeu_id})

    try:
        commentaire = CommentaireJeu.objects.filter(jeu=jeu).get(id=id)
    except CommentaireJeu.DoesNotExist:
        return render(request, "commentaires/not_found.html", {"id": id})

    return render(
        request, "commentaires/view.html", {"commentaire": commentaire, "jeu": jeu}
    )


def edit(request: HttpRequest, jeu_id: int, id: int):
    """Modifie un commentaire."""
    try:
        jeu = Jeu.objects.get(id=jeu_id)
    except Jeu.DoesNotExist:
        return render(request, "jeux/not_found.html", {"id": jeu_id})

    try:
        commentaire = CommentaireJeu.objects.filter(jeu=jeu).get(id=id)
    except CommentaireJeu.DoesNotExist:
        return render(request, "commentaires/not_found.html", {"id": id})

    if request.method == "GET":
        return render(
            request,
            "commentaires/edit.html",
            {
                "form": CommentaireNoJoueurForm(instance=commentaire),
                "jeu": jeu,
                "commentaire": commentaire,
            },
        )

    if request.method == "POST":
        form = CommentaireNoJoueurForm(request.POST, instance=commentaire)
        if form.is_valid():
            form.save()
        else:
            return render(request, "commentaires/edit.html", {"form": form, "jeu": jeu})

    return view(request, jeu_id, id)


def delete(request: HttpRequest, jeu_id: int, id: int):
    """Supprime un commentaire."""
    try:
        jeu = Jeu.objects.get(id=jeu_id)
    except Jeu.DoesNotExist:
        return render(request, "jeux/not_found.html", {"id": jeu_id})

    try:
        commentaire = CommentaireJeu.objects.filter(jeu=jeu).get(id=id)
    except CommentaireJeu.DoesNotExist:
        return render(request, "commentaires/not_found.html", {"id": id})

    commentaire.delete()
    return all(request, jeu_id)
