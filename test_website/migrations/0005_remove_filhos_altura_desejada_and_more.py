# Generated by Django 4.2.4 on 2023-08-31 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_website', '0004_remove_pais_altura_desejada_remove_pais_escola_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filhos',
            name='altura_desejada',
        ),
        migrations.RemoveField(
            model_name='filhos',
            name='largura_desejada',
        ),
    ]