# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Ocupacao(models.Model):
    nome = models.CharField(max_length=250)
    descricao = models.CharField(max_length=350)
    imagem = models.CharField(max_length=500)

class Pessoa(models.Model):
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE())
    nome = models.CharField(max_length=250)
    Telefone = models.CharField(max_length=350)
    
