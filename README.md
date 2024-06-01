# SAE2.01

## Installation du projet

> [!IMPORTANT]
> Il peut-être nécessaire d'installer l'outil `pdm` pour installer correctement le projet.
> Cela est dû à un problème avec l'outil par défaut, `setuptools`, ayant du mal à supporter

Créer un environnement virtuel :

```cmd
python -m venv .venv
```

Pour l'activer :

```cmd
# Sur Windows
.venv\Scripts\activate
# Sur Linux
. .venv\bin\activate
```

Pour installer le projet :

```cmd
pip install .

# Avec des dépendances pour le développement :
pip install .[dev]
```

## Mise en production

Sur le serveur hébergent le serveur Django, il faut paramétrer les environments de variables suivants :

- `DJANGO_SECRET_KEY` : Une clé à garder secrète.
- `DJANGO_DEBUG` : Uniquement sur `True` pour activer le mode production. (Serveur PostgreSQL)
- `DJANGO_POSTGRES_NAME` : Nom de la base de donnée.
- `DJANGO_POSTGRES_USER` : Utilisateur de la DB.
- `DJANGO_POSTGRES_PASSWORD` : Mot de passe de l'utilisateur.
- `DJANGO_POSTGRES_NAME` : L'hôte de la DB.
- `DJANGO_POSTGRES_NAME` : Le port du serveur, par défaut `5432`.
