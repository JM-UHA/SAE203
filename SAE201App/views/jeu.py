from django.http import HttpRequest
from django.shortcuts import render
from ..forms import JeuForm

def create(request):
    """ajouter un jeu"""
    if request.method == "Envoyer":
        form = JeuForm(request)
        if form.is_valid():
            Jeu = form.save()
            return render(request,"jeu/view.html",{"jeu" : Jeu})
        else:
            return render(request,"jeu/create.html",{"form": form})
    else:
        form = JeuForm()
        return render(request,"jeu/create.html",{"form":form})
def view(request,id):
    """permet de voir une fiche de jeu"""
    jeu = Jeu.object.get(pk=id)
    return render(request, "jeu/view.html", {"jeu": jeu})
def all(request: HttpRequest, jeu_id: int, id: int):
    """permet de voir l'ensemble des jeux"""
    jeu = Jeu.object.filter()
    return render(request, "jeu/all.html", {"jeu": jeu})

def edit(request: HttpRequest, jeu_id: int, id: int):
    """Permet de modifier la fiche d'un jeu"""
    try:
        jeu = Jeu.objects.get(id=id)
    except Jeu.DoesNotExist:
        return render(request, "jeu/not_found.html", {"id": id})
    if request.method == "POST":
        form = JeuForm(request.POST, instance=jeu)
        if form.is_valid():
            form.save()
        else:
            return render(request, "jeu/edit.html", {"form": form})
    return view(request, jeu_id, id)

def delete(request: HttpRequest, jeu_id: int, id: int):
    """permet de supprimer un jeu"""
    try:
        jeu = Jeu.objects.get(id=id)
    except Jeu.DoesNotExist:
        return render(request, "jeu/not_found.html", {"id": id})
    jeu.delete()
    return all(request)
