from django.http import HttpRequest
from django.shortcuts import render

from ..forms import AuteurForm
from ..models import Auteur


def create(request: HttpRequest, auteur_id: int):
    """ajouter un auteur"""
    if request.method == "GET":
        return render(request, "auteurs/create.html", {"form": AuteurForm()})
    if request.method == "POST":
        form = AuteurForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, "auteurs/create.html", {"form": form})

    return all(request, auteur_id)


def view(request: HttpRequest, auteur_id: int, id: int):
    """permet de voir une fiche auteur"""
    try:
        auteur = Auteur.objects.get(id=id)
    except Auteur.DoesNotExist:
        return render(request, "auteurs/not_found.html", {"id": id})

    return render(request, "auteurs/view.html", {"auteur": auteur})


def edit(request: HttpRequest, auteur_id: int, id: int):
    """permet de modifier une fiche auteur"""
    try:
        auteur = Auteur.objects.get(id=id)
    except Auteur.DoesNotExist:
        return render(request, "auteurs/not_found.html", {"id": id})

    if request.method == "POST":
        form = AuteurForm(request.POST, instance=auteur)
        if form.is_valid():
            form.save()
        else:
            return render(request, "auteurs/edit.html", {"form": form})

    return view(request, auteur_id, id)


def delete(request: HttpRequest, auteur_id: int, id: int):
    """permet de supprimer une fiche auteur"""
    try:
        auteur = Auteur.objects.get(id=id)
    except Auteur.DoesNotExist:
        return render(request, "auteurs/not_found.html", {"id": id})

    auteur.delete()
    return all(request, auteur_id)


def all(request: HttpRequest, auteur_id: int):
    """permet de voir l'ensemble des fiches auteur"""
    auteur = Auteur.objects.filter()
    return render(request, "auteurs/all.html", {"auteur": auteur})
