from django.http import HttpRequest
from django.shortcuts import render

from .forms import AuteursForm


def ajout(request: HttpRequest):
    if request.method == "POST":
        form = AuteursForm(request.POST)
        if form.is_valid():
            auteurs = form.save()
            return render(request, "SAE201App/formulaire_auteurs.html", {"Auteur": auteurs})
        else:
            form = AuteursForm()
            return render("formulaire/ajout.html",{"form": form})

# Create your views here.
