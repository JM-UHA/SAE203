from django.http import HttpRequest
from django.shortcuts import render

from SAE201App.models import Jeu

from ..forms import JeuForm


def all(request: HttpRequest):
    """permet de voir l'ensemble des jeux"""
    jeu = Jeu.objects.filter()
    return render(request, "jeux/all.html", {"jeu": jeu})


def create(request: HttpRequest):
    """ajouter un jeu"""
    if request.method == "GET":
        return render(request, "jeux/create.html", {"form": JeuForm()})

    if request.method == "POST":
        form = JeuForm(request.POST)
        if form.is_valid():
            jeu = form.save()
            return view(request, jeu.pk)
        else:
            return render(request, "jeux/create.html", {"form": form})

    return all(request)


def view(request: HttpRequest, id: int):
    """permet de voir une fiche de jeu"""
    jeu = Jeu.objects.get(pk=id)
    return render(request, "jeux/view.html", {"jeu": jeu})


def edit(request: HttpRequest, id: int):
    """Permet de modifier la fiche d'un jeu"""
    try:
        jeu = Jeu.objects.get(id=id)
    except Jeu.DoesNotExist:
        return render(request, "jeux/not_found.html", {"id": id})

    if request.method == "POST":
        form = JeuForm(request.POST, instance=jeu)
        if form.is_valid():
            form.save()
        else:
            return render(request, "jeux/edit.html", {"form": form})

    return view(request, id)


def delete(request: HttpRequest, id: int):
    """permet de supprimer un jeu"""
    try:
        jeu = Jeu.objects.get(id=id)
    except Jeu.DoesNotExist:
        return render(request, "jeux/not_found.html", {"id": id})

    jeu.delete()
    return all(request)
