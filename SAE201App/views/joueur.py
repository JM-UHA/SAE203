from django.http import HttpRequest
from django.shortcuts import render

from ..forms import JoueurForm

def create(request: HttpRequest, joueur_id: int):
    """Sert à ajouter un joueur"""
    if request.method == "Envoyer":
        form = JoueurForm(request)
        if form.is_valid():
            Joueur = form.save()
            return render(request,"joueur/view.html",{"joueur" : Joueur})
        else:
            return render(request,"joueur/create.html",{"form": form})
    else:
        form = JoueurForm()
        return render(request,"joueur/create.html",{"form":form})

def view(request: HttpRequest, joueur_id: int, id: int):
    """permet de voir une fiche joueur"""
    try:
        joueur = Joueur.objects.get(id=id)
    except Joueur.DoesNotExist:
        return render(request, "joueur/not_found.html", {"id": id})
    return render(request, "joueur/view.html", {"joueur": joueur})


def edit(request: HttpRequest, joueur_id: int, id: int):
    """Permet de modifier une fiche joueur"""
    try:
        joueur = Joueur.objects.get(id=id)
    except Joueur.DoesNotExist:
        return render(request, "joueur/not_found.html", {"id": id})
    if request.method == "POST":
        form = JoueurForm(request.POST, instance=joueur)
        if form.is_valid():
            form.save()
        else:
            return render(request, "joueur/edit.html", {"form": form})
    return view(request, joueur_id, id)

def delete(request: HttpRequest, joueur_id: int, id: int):
    """permet de supprimer une fiche joueur"""
    try:
        joueur = Joueur.objects.get(id=id)
    except Joueur.DoesNotExist:
        return render(request, "joueur/not_found.html", {"id": id})
    joueur.delete()
    return all(request)

def all(request: HttpRequest, joueur_id: int, id: int):
    """permet de voir l'ensemble des fiches joueur"""
    joueur = Joueur.object.filter()
    return render(request, "joueur/all.html", {"joueur": joueur})
