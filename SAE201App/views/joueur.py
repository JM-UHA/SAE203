from django.shortcuts import render
from ..forms import JoueurForm

def ajouter_joueur(request):
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

def read_joueur(request,id):
    """permet de voir une fiche joueur"""
    joueur = models.joueur.object.get(pk=id)
    return render(request, "joueur/view.html", {"Joueur": joueur})
