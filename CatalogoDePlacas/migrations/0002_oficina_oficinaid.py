# Generated by Django 5.0 on 2023-12-11 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CatalogoDePlacas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='oficina',
            name='oficinaId',
            field=models.IntegerField(default=1),
        ),
    ]