# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from modelos.usuario.models import Usuario

# Create your models here.

class Funcionario(models.Model):

	usuario = models.ForeignKey(Usuario, null = False, blank = False, on_delete= models.CASCADE)
	numero_documento = models.CharField('ID', primary_key=True, max_length=30) 
	tipo_documento = models.CharField(max_length=30)
	nombre = models.CharField(max_length=50)
	appellido =  models.CharField(max_length=50)
	telefono = models.CharField(max_length=20)
	