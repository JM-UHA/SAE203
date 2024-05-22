from django.http import HttpRequest
from django.shortcuts import render

from ..forms import AuteursForm


def ajout(request: HttpRequest):
    """ajouter un auteurs"""
    if request.method == "POST":
        form = AuteursForm(request.POST)
        if form.is_valid():
            auteurs = form.save()
            return render(request, "SAE201App/formulaire_auteurs.html", {"Auteur": auteurs})
        else:
            form = AuteursForm()
            return render("auteurs/ajout.html",{"form": form})
def traitement(request):
    lform = AuteursForm(request.POST)
    if lform.is_valid():
        Auteurs = lform.save()
        return render(request,"formulaire_auteurs.html",{"Auteurs": Auteurs})
    else:
        return render(request,"f")
# Create your views here.
