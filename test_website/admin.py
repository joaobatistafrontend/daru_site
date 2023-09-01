from django.contrib import admin
from .models import *

@admin.register(Escola)
class EscolaAdmin(admin.ModelAdmin):
    list_display = ['nome','cnpj','telefone', 'email','bairro','cidade','rua','logradouro','cep']

@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ['nome','cpf','telefone', 'email','bairro','cidade','rua','logradouro','cep']

@admin.register(Filhos)
class FilhosAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(Visitante)
class VisitantesAdmin(admin.ModelAdmin):
    list_display = ['nome','cpf','telefone','data_cadastro']
