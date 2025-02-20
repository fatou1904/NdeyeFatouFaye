# Generated by Django 5.1.6 on 2025-02-20 12:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tache', '0006_remove_tache_assigne_a_remove_tache_auteur_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='tache',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='taches_assignees', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tache',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taches_creees', to=settings.AUTH_USER_MODEL),
        ),
    ]
