from django.contrib import admin
from .models import LogoEmpresa

class LogoEmpresaAdmin(admin.ModelAdmin):
	""" Admin de logos de las empresas """
	list_display = ('titulo', 'imagen', 'creado_en', 'modificado_en')
	list_display_links = ('titulo',)
	list_filter = ('creado_en', 'modificado_en',)
	search_fields = ['titulo', 'creado_en', 'modificado_en']

admin.site.register(LogoEmpresa, LogoEmpresaAdmin)