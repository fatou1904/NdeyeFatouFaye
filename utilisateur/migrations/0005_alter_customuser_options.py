# Generated by Django 5.1.6 on 2025-02-20 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0004_alter_customuser_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]
