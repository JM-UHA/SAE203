# Generated by Django 5.0.6 on 2024-06-01 23:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("SAE201App", "0004_alter_jeu_auteur_alter_jeu_editeur_alter_jeu_titre"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jeu",
            name="auteur",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="SAE201App.auteur"
            ),
        ),
        migrations.AlterField(
            model_name="joueur",
            name="mail",
            field=models.EmailField(max_length=254),
        ),
    ]
