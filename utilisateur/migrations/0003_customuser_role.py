# Generated by Django 5.1.6 on 2025-02-19 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0002_customuser_datecreation'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('etudiant', 'Étudiant'), ('professeur', 'Professeur')], default='etudiant', max_length=10),
        ),
    ]
