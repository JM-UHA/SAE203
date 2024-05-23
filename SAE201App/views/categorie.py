from django.http import HttpRequest
from django.shortcuts import render

from ..forms import CategorieForm

def all(request: HttpRequest, categorie_id: int):
    """affiche toutes les catégories."""
    categorie = Categorie.object.filter()
    return render(request, "categorie/all.html", {"categorie": categorie})

def create(request: HttpRequest, categorie_id: int):
    """Sert à ajouter une categorie"""
    if request.method == "Envoyer":
        form = CategorieForm(request)
        if form.is_valid():
            Categorie = form.save()
            return render(request,"categorie/view.html",{"categorie" : Categorie})
        else:
            return render(request,"categorie/create.html",{"form": form})
    else:
        form = CategorieForm()
        return render(request,"categorie/create.html",{"form":form})

def view(request: HttpRequest, categorie_id: int, id: int):
    """permet de voir une catégorie"""
    try:
        categorie = Categorie.objects.get(id=id)
    except Categorie.DoesNotExist:
        return render(request, "categorie/not_found.html", {"id": id})
    return render(request, "categorie/view.html", {"categorie": categorie})

def edit(request: HttpRequest, categorie_id: int, id: int):
    """Permet de modifier une catégorie"""
    try:
        categorie = Categorie.objects.get(id=id)
    except Categorie.DoesNotExist:
        return render(request, "categorie/not_found.html", {"id": id})
    if request.method == "POST":
        form = CategorieForm(request.POST, instance=categorie)
        if form.is_valid():
            form.save()
        else:
            return render(request, "categorie/edit.html", {"form": form})
    return view(request, c_id, id)

def delete(request: HttpRequest, categorie_id: int, id: int):
    """permet de supprimer une catégorie"""
    try:
        categorie = Categorie.objects.get(id=id)
    except Categorie.DoesNotExist:
        return render(request, "categorie/not_found.html", {"id": id})
    categorie.delete()
    return all(request)
