from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as DefaultUserManager




def upload_to():
     filho_nome = Filhos.nome     
     return f'uploads/{filho_nome}/fotos'



class Escola(models.Model):
     nome = models.CharField("Escola", max_length=100)
     cnpj = models.CharField("CNPJ", max_length=18, unique=True)
     telefone = models.CharField(max_length=15, verbose_name="Telefones")
     email = models.EmailField("Email", max_length=120)
     bairro = models.CharField("Bairro", max_length=200)
     cidade = models.CharField("cidade", max_length=200)
     rua = models.CharField("Rua", max_length=200)
     logradouro = models.CharField("Logradouro", max_length=200)
     cep = models.CharField("Cep", max_length=200)

     def __str__(self):
          return self.nome

class Pais(models.Model):
     nome = models.CharField(max_length=100, verbose_name="Responsaveis")
     cpf = models.CharField("CPF",max_length=14, unique=True)
     telefone = models.CharField(max_length=15, verbose_name="Telefones")
     email = models.EmailField("Email", max_length=120)
     foto = models.ImageField("Foto", upload_to='responsaveis/')
     email = models.EmailField("Email", max_length=120)
     bairro = models.CharField("Bairro", max_length=200)
     cidade = models.CharField("cidade", max_length=200)
     rua = models.CharField("Rua", max_length=200)
     logradouro = models.CharField("Logradouro", max_length=200)
     cep = models.CharField("Cep", max_length=200)
     #a escola pode ter varios responsaveis mais o reponsavel pode ter apenas 1 escola
     #escola = models.OneToOneField(Escola, on_delete=models.CASCADE)

     def __str__(self):
        return self.nome
             

class Visitante(models.Model, DefaultUserManager):
     nome = models.CharField("Visitante", max_length=100)
     cpf = models.CharField("CPF", max_length=14, unique=True)
     telefone = models.CharField("Telefone",max_length=15)
     foto = models.ImageField("Foto", upload_to='visitantes__autorizados/')
     data_cadastro = models.DateTimeField("Hora de ativaçao", default=timezone.now)
     responsavel =  models.OneToOneField(Pais, on_delete=models.CASCADE)
     #o visitante pode ter apenas 1 responsavel          
     
     def __str__(self):
          return self.nome

     def save(self, *args, **kwargs):
          super().save(*args, **kwargs)
          self.excluir_apos_2_minutos()

     def excluir_apos_2_minutos(self):
          if timezone.now() - self.data_cadastro > timedelta(minutes=2):
               self.delete()





     #def is_active(self):
     #     return timezone.now() - self.data_cadastro > timedelta(minutes=1)#horas = (hours=12)
     #desativasao do visitante

class Filhos(models.Model):
     responsavel = models.ManyToManyField(Pais, verbose_name="Alunos")
     visitante = models.OneToOneField(Visitante, on_delete=models.CASCADE, blank=True, null=True)
     nome = models.CharField("Nome", max_length=100)
     foto = models.ImageField("Foto", upload_to='visitantes__autorizados/')
     #o filho pode ter varios responsavel
     #mais so pode ter 1 visitante 

     def __str__(self):
          return self.nome

