from django.http import HttpRequest
from django.shortcuts import render

from ..forms import AuteurForm


def create(request: HttpRequest, jeu_id: int):
    """ajouter un auteur"""
    if request.method == "POST":
        form = AuteurForm(request.POST)
        if form.is_valid():
            auteurs = form.save()
            return render(request, "auteur/create.html", {"auteur": auteurs})
        else:
            form = AuteurForm()
            return render(request,"auteurs/create.html",{"form": form})
def view(request: HttpRequest, auteur_id: int, id: int):
    """permet de voir une fiche auteur"""
    try:
        auteur = Auteur.objects.get(id=id)
    except Auteur.DoesNotExist:
        return render(request, "auteur/not_found.html", {"id": id})
    return render(request, "auteur/view.html", {"auteur": auteur})
def edit(request: HttpRequest, auteur_id: int, id: int):
    """permet de modifier une fiche auteur"""
    try:
        auteur = Auteur.objects.get(id=id)
    except Auteur.DoesNotExist:
        return render(request, "auteur/not_found.html", {"id": id})
    if request.method == "POST":
        form = AuteurForm(request.POST, instance=auteur)
        if form.is_valid():
            form.save()
        else:
            return render(request, "auteur/edit.html", {"form": form})
    return view(request, auteur_id, id)

def delete(request: HttpRequest, auteur_id: int, id: int):
    """permet de supprimer une fiche auteur"""
    try:
        auteur = Auteur.objects.get(id=id)
    except auteur.DoesNotExist:
        return render(request, "auteur/not_found.html", {"id": id})
    auteur.delete()
    return all(request)

def all(request: HttpRequest, auteur_id: int, id: int):
    """permet de voir l'ensemble des fiches auteur"""
    auteur = Auteur.object.filter()
    return render(request, "auteur/all.html", {"auteur": auteur})
