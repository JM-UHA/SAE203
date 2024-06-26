import io
import json
import typing

from django.http import HttpRequest
from django.shortcuts import render

from SAE201App.models import Auteur, Jeu

from ..forms import ImportJeu, JeuForm


def all(request: HttpRequest):
    """Permet l'affichage globale de tout les jeux."""
    jeux = Jeu.objects.all()
    return render(request, "jeux/all.html", {"jeux": jeux})


def create(request: HttpRequest):
    """Ajoute un jeu."""
    if request.method == "GET":
        return render(request, "jeux/create.html", {"form": JeuForm()})

    if request.method == "POST":
        form = JeuForm(request.POST, request.FILES)
        if form.is_valid():
            jeu = form.save()
            return view(request, jeu.pk)
        else:
            return render(request, "jeux/create.html", {"form": form})

    return all(request)


def view(request: HttpRequest, id: int):
    """Permet de voir en détail les informations d'un jeu."""
    jeu = Jeu.objects.get(pk=id)
    return render(request, "jeux/view.html", {"jeu": jeu})


def edit(request: HttpRequest, id: int):
    """Permet de modifier la fiche d'un jeu."""
    try:
        jeu = Jeu.objects.get(id=id)
    except Jeu.DoesNotExist:
        return render(request, "jeux/not_found.html", {"id": id})

    if request.method == "GET":
        form = JeuForm(instance=jeu)
        return render(request, "jeux/edit.html", {"form": form, "jeu": jeu})

    if request.method == "POST":
        form = JeuForm(request.POST, request.FILES, instance=jeu)
        if form.is_valid():
            form.save()
        else:
            return render(request, "jeux/edit.html", {"form": form, "jeu": jeu})

    return view(request, id)


def delete(request: HttpRequest, id: int):
    """Supprime un jeu."""
    try:
        jeu = Jeu.objects.get(id=id)
    except Jeu.DoesNotExist:
        return render(request, "jeux/not_found.html", {"id": id})

    jeu.delete()
    return all(request)


def import_jeu(request: HttpRequest):
    """Permet d'ajouter des jeux via un fichier JSON."""

    class ImportResult(typing.TypedDict):
        data: typing.List[Jeu]
        errors: list[str] | None

    def process_fichier(fichier: typing.Any) -> ImportResult:
        donnees = io.StringIO(fichier.read().decode("utf-8"))
        try:
            in_json = json.load(donnees)
        except json.JSONDecodeError:
            return {
                "data": [],
                "errors": [f"Impossible de lire le fichier. Est-ce bien un JSON ?"],
            }

        if not in_json.get("jeux"):
            return {
                "data": [],
                "errors": [
                    'Aucun jeu trouvé dans le fichier. Un clé "jeux" doit exister.'
                ],
            }
        if not isinstance(in_json["jeux"], list):
            return {"data": [], "errors": ['La clé "jeux" doit être une liste.']}

        final: typing.List[Jeu] = []
        errors: typing.List[str] = []

        for index, jeu in enumerate(in_json["jeux"], start=1):
            if not isinstance(jeu, dict):
                errors.append(f"Jeu N.{index}, le jeu {jeu} n'est pas un dictionnaire.")
                continue
            jeu = typing.cast(typing.Dict[str, typing.Any], jeu)
            if not jeu.get("titre"):
                errors.append(f'Jeu N.{index}, "titre" manquant.')
                continue
            if not jeu.get("annee"):
                errors.append(f'Jeu N.{index}, "annee" manquante.')
                continue
            if not isinstance(jeu["annee"], int):
                errors.append(f'Jeu N.{index}, "annee" doit être un chiffre.')
                continue
            if not jeu.get("editeur"):
                errors.append(f'Jeu N.{index}, "editeur" manquant.')
                continue
            if not jeu.get("auteur"):
                errors.append(f'Jeu N.{index}, "auteur" manquant.')
                continue
            if not isinstance(jeu["auteur"], list):
                errors.append(f'Jeu N.{index}, "auteur" n\'est pas une liste.')
                continue
            if not len(jeu["auteur"]) == 2:  # type: ignore
                errors.append(f'Jeu N.{index}, "auteur" doit contenir 2 éléments.')
                continue
            try:
                jeu_auteur = Auteur.objects.filter(nom=jeu["auteur"][0], prenom=jeu["auteur"][1]).first()
            except Auteur.DoesNotExist:
                errors.append(f'Jeu N.{index}, l\'auteur {jeu["auteur"][0]} {jeu["auteur"][1]} n\'existe pas.')
                continue

            final.append(
                Jeu(
                    titre=jeu["titre"],
                    annee=jeu["annee"],
                    editeur=jeu["editeur"],
                    auteur=jeu_auteur,
                    categorie=None,
                    photo=None,
                )
            )

        return {"data": final, "errors": errors}

    if request.method == "GET":
        return render(request, "jeux/import.html", {"form": ImportJeu()})

    elif request.method == "POST":
        form = ImportJeu(request.POST, request.FILES)
        if form.is_valid():
            fichier = form.cleaned_data["fichier"]
            donnees = process_fichier(fichier)

            for jeu in donnees["data"]:
                jeu.save()

            # Après process
            return render(
                request,
                "jeux/review_import.html",
                {"data": donnees["data"], "errors": donnees["errors"]},
            )
        else:
            return render(request, "jeux/import.html", {"form": form})

    return all(request)
