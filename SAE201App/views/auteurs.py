from django.http import HttpRequest
from django.shortcuts import render

from ..forms import AuteursForm


def ajout(request: HttpRequest):
    """ajouter un auteurs"""
    if request.method == "POST":
        form = AuteursForm(request.POST)
        if form.is_valid():
            auteurs = form.save()
            return render(request, "SAE201App/create.html", {"Auteur": auteurs})
        else:
            form = AuteursForm()
            return render("auteurs/create.html",{"form": form})
def traitement(request):
    lform = AuteursForm(request.POST)
    if lform.is_valid():
        Auteurs = lform.save()
        return render(request,"/auteurs/create.html",{"Auteurs": Auteurs})
    else:
        return render(request,"/auteurs/view.html", {"form": lform})
# Create your views here.
def read(request, id):
    Auteur = models.Auteurs.objects.get(pk=id)
    return render(request, "auteurs/view.html", {"Auteur": Auteur})
def traitementupdate(request,id):
    lform =AuteursForm(request.POST)
    if lform.is_valid():
        Auteur = lform.save(commit=False)
        Auteur.id = id;
        Auteur.save()
        return HttpResponseRedirect("/auteur/")
    else:
        return render(request, "auteurs/edit.html" , {"form": lform, "id" : id})
