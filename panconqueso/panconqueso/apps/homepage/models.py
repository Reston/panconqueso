#-*- coding: utf-8
from django.db import models

class LogoEmpresa(models.Model):
	""" Logo de las empresas para el inicio de la página """
	titulo = models.CharField(max_length=50)
	imagen = models.ImageField(upload_to='imgLogo', help_text='Tamaño 225x225px recomendado para evitar distorción')
	creado_en = models.DateTimeField(auto_now_add=True, editable=False)
	modificado_en = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.titulo

	def __str__(self):
		return (self.titulo).encode('ascii', errors='replace') #evitar error raro en admin