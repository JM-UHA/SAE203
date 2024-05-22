# SAE2.01

## Installation du projet

> [!IMPORTANT]
> Il peut-être nécessaire d'installer l'outil `pdm` pour installer correctement le projet.
> Cela est dû à un probleme avec l'outil par défaut, `setuptools`, ayant du mal à supporter 

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
