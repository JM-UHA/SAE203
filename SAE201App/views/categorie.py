from django.http import HttpRequest
from django.shortcuts import render

from SAE201App.models import CategorieJeu

from ..forms import CategorieForm


def all(request: HttpRequest):
    """affiche toutes les catégories."""
    categorie = CategorieJeu.objects.all()
    return render(request, "categories/all.html", {"categories": categorie})


def create(request: HttpRequest):
    """Sert à ajouter une categorie"""
    if request.method == "GET":
        return render(request, "categories/create.html", {"form": CategorieForm()})

    if request.method == "POST":
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, "categories/create.html", {"form": form})

    return all(request)


def view(request: HttpRequest, id: int):
    """permet de voir une catégorie"""
    try:
        categorie = CategorieJeu.objects.get(id=id)
    except CategorieJeu.DoesNotExist:
        return render(request, "categories/not_found.html", {"id": id})

    return render(request, "categories/view.html", {"categorie": categorie})


def edit(request: HttpRequest, id: int):
    """Permet de modifier une catégorie"""
    try:
        categorie = CategorieJeu.objects.get(id=id)
    except CategorieJeu.DoesNotExist:
        return render(request, "categories/not_found.html", {"id": id})

    if request.method == "GET":
        form = CategorieForm(instance=categorie)
        return render(
            request, "categories/edit.html", {"form": form, "categorie": categorie}
        )

    if request.method == "POST":
        form = CategorieForm(request.POST, request.FILES, instance=categorie)
        if form.is_valid():
            form.save()
        else:
            return render(
                request, "categories/edit.html", {"form": form, "categorie": categorie}
            )

    return view(request, id)


def delete(request: HttpRequest, id: int):
    """permet de supprimer une catégorie"""
    try:
        categorie = CategorieJeu.objects.get(id=id)
    except CategorieJeu.DoesNotExist:
        return render(request, "categories/not_found.html", {"id": id})

    categorie.delete()
    return all(request)
