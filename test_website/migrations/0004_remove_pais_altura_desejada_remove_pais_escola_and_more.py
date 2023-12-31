# Generated by Django 4.2.4 on 2023-08-31 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_website', '0003_alter_pais_cep'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pais',
            name='altura_desejada',
        ),
        migrations.RemoveField(
            model_name='pais',
            name='escola',
        ),
        migrations.RemoveField(
            model_name='pais',
            name='largura_desejada',
        ),
        migrations.RemoveField(
            model_name='visitante',
            name='altura_desejada',
        ),
        migrations.RemoveField(
            model_name='visitante',
            name='largura_desejada',
        ),
        migrations.AlterField(
            model_name='pais',
            name='cpf',
            field=models.CharField(max_length=14, unique=True, verbose_name='CPF'),
        ),
    ]
