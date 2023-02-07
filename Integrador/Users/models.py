from distutils.command.upload import upload
from django.db import models,migrations
from django.db.models import signals
from django.template.defaultfilters import slugify
from django import forms
import django.core.files.storage

#pip install django-stdimage
# or
#pipenv install django-stdimage
from stdimage import StdImageField, JPEGField

# Create your models here.
Sexo_Choices = (
    ('M','Masculino'),
    ('F','Feminino'),
)

Cargo_Choices = (
    ('0','None'),
    ('1','Discente'),
    ('2','Docente'),
    ('3','Tercerizado'),
    ('4','Bolsista'),     
    ('5','Reitor'),
)

Eleicao_Cargo_Choices=( ('1','Todos'),
                        ('2','Discentes'),
                        ('3','Docentes'),
                        ('4','Reitores'),
                        (5,'Tercerizado'),
                        ('6','Bolsistas'),
                        ('7','Dicentes  & Bolsistas'),
                        ('8','Dicentes & Docentes'),
                        ('9','Docentes & Reitores'),
                        ('10','Discentes & Tercerizados'),
                        ('11','Docentes, Reitores & Bolsistas'),
                        ('12','Discente, Docentes & Bolsistas'),
                        ('13','Docentes, Reitores & Tercerizados'),
                        ('14','Discentes, Bolsistas & Tercerizados'),
                        ('15','Docentes, Reitores, Bolsistas & Tercerizados'),
                        ('16','Docentes, Reitores, Discentes & Tercerizados'),
)



Titulo_Choices = (
    ('1','Problema com uma eleição'),
    ('2','Problema com Site'),
    ('3','Problema com conta'),    
)


class User(models.Model):
    Id_Academico = models.CharField(max_length=15,unique=True,primary_key=True)
    Nome = models.CharField(max_length=50,null = False)
    CPF = models.CharField(max_length=11,unique=True,null=False)
    Genero =models.CharField(max_length=1,choices=Sexo_Choices)
    email = models.EmailField(blank=True,null=True)
    Senha = models.CharField(max_length=300)
    Foto= models.ImageField('Imagem do perfil', upload_to='profile', default=None)
    Cargo =models.CharField(max_length=1,choices=Cargo_Choices)
    Foto_Cargo= models.ImageField('Cargo info', upload_to='Cargo_profile', default=None)
    def __str__(self):
        return self.Id_Academico


class Election(models.Model):
    N_Eleicao = models.IntegerField(unique=True,primary_key=True,auto_created=True)
    Usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    Titulo = models.CharField(max_length=30, null = False)
    Data = models.DateField(null= True)
    End_Data = models.DateField(null= True)
    Descricao = models.CharField(max_length=150,null = True)
    Ativo = models.BooleanField()
    Cargo =models.CharField(max_length=2,choices=Eleicao_Cargo_Choices)
    

    def __str__(self) -> str:
        return super().__str__()

    '''def __str__(self):
        return  str(self.N_Eleicao)'''

class Activity_Report(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(blank=True,null=True)
    titulo =models.CharField(max_length=1,choices=Titulo_Choices)
    balao  = models.CharField(max_length=300,null =False)


    def __str__(self) -> str:
        return super().__str__()

class Data_Election(models.Model):
    N_Eleicao = models.ForeignKey(Election,on_delete=models.CASCADE,unique=False)
    Candidatos = models.CharField(max_length=50)
    N_Candidato = models.IntegerField()
    Votos = models.IntegerField(null = False)


    def __str__(self) -> str:
        return super().__str__()
    '''def __str__(self):
        return str(self.N_Eleicao)'''

class Interaction_User(models.Model):
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    N_Eleicao = models.ForeignKey(Election,on_delete=models.CASCADE)
    Data = models.DateField()

    def __str__(self) -> str:
        return super().__str__()
