from django.shortcuts import render
from .forms import AuteursForm
from . import  models

def ajout(request):
    if request.method == 'POST'
        form = AuteursForm(request)
        if form.is_valid():
            Auteurs = form.save()
            return render(request, "SAE201App/affiche.html"),{"Auteur" : Auteurs})

# Create your views here.
