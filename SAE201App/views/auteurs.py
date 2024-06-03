from django.http import HttpRequest
from django.shortcuts import render

from ..forms import AuteurForm
from ..models import Auteur

def all(request: HttpRequest):
    """permet de voir l'ensemble des fiches auteur"""
    auteurs = Auteur.objects.all()
    return render(request, "auteurs/all.html", {"auteurs": auteurs})


def create(request: HttpRequest):
    """ajouter un auteur"""
    if request.method == "GET":
        return render(request, "auteurs/create.html", {"form": AuteurForm()})

    if request.method == "POST":
        form = AuteurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            return render(request, "auteurs/create.html", {"form": form})

    return all(request)


def view(request: HttpRequest, id: int):
    """permet de voir une fiche auteur"""
    try:
        auteur = Auteur.objects.get(id=id)
    except Auteur.DoesNotExist:
        return render(request, "auteurs/not_found.html", {"id": id})

    print(vars(auteur.photo))
    return render(request, "auteurs/view.html", {"auteur": auteur})


def edit(request: HttpRequest, id: int):
    """permet de modifier une fiche auteur"""
    try:
        auteur = Auteur.objects.get(id=id)
    except Auteur.DoesNotExist:
        return render(request, "auteurs/not_found.html", {"id": id})

    if request.method == "GET":
        form = AuteurForm(instance=auteur)
        return render(request, "auteurs/edit.html", {"form": form, "auteur": auteur})

    if request.method == "POST":
        form = AuteurForm(request.POST, request.FILES, instance=auteur)
        if form.is_valid():
            form.save()
        else:
            return render(request, "auteurs/edit.html", {"form": form, "auteur": auteur})

    return view(request, id)


def delete(request: HttpRequest, id: int):
    """permet de supprimer une fiche auteur"""
    try:
        auteur = Auteur.objects.get(id=id)
    except Auteur.DoesNotExist:
        return render(request, "auteurs/not_found.html", {"id": id})

    auteur.delete()
    return all(request)
