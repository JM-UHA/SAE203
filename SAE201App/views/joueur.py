from django.http import HttpRequest
from django.shortcuts import render

from SAE201App.models import Joueur

from ..forms import JoueurForm


def all(request: HttpRequest):
    """permet de voir l'ensemble des fiches joueur"""
    joueurs = Joueur.objects.all()
    return render(request, "joueurs/all.html", {"joueurs": joueurs})


def create(request: HttpRequest):
    """Sert à ajouter un joueur"""
    if request.method == "GET":
        return render(request, "joueurs/create.html", {"form": JoueurForm()})

    if request.method == "POST":
        form = JoueurForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, "joueurs/create.html", {"form": form})

    return all(request)


def view(request: HttpRequest, id: int):
    """permet de voir une fiche joueur"""
    try:
        joueur = Joueur.objects.get(id=id)
    except Joueur.DoesNotExist:
        return render(request, "joueurs/not_found.html", {"id": id})

    return render(request, "joueurs/view.html", {"joueur": joueur})


def edit(request: HttpRequest, id: int):
    """Permet de modifier une fiche joueur"""
    try:
        joueur = Joueur.objects.get(id=id)
    except Joueur.DoesNotExist:
        return render(request, "joueurs/not_found.html", {"id": id})

    if request.method == "GET":
        form = JoueurForm(instance=joueur)
        return render(request, "joueurs/edit.html", {"form": form, "joueur": joueur})

    if request.method == "POST":
        form = JoueurForm(request.POST, instance=joueur)
        if form.is_valid():
            form.save()
        else:
            return render(request, "joueurs/edit.html", {"form": form, "joueur": joueur})
    return view(request, id)


def delete(request: HttpRequest, id: int):
    """permet de supprimer une fiche joueur"""
    try:
        joueur = Joueur.objects.get(id=id)
    except Joueur.DoesNotExist:
        return render(request, "joueurs/not_found.html", {"id": id})
    joueur.delete()
    return all(request)
