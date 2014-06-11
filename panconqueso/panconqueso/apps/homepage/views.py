#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from panconqueso.apps.homepage.forms import contactForm
from django.template import RequestContext
from django.core.mail import send_mail
from instagram.client import InstagramAPI


def index(request):
	success = False
	if request.method == 'POST':
		form = contactForm(request.POST)
		if form.is_valid():
			success = True
			cd = form.cleaned_data
			asunto = u'Por: %s mail: %s Tipo de servicio: %s Plan: %s' % (cd['nombre'], cd['email'], cd['tipoServicio'], cd['planes'])
			content = u'Email contacto: %s \nAsunto: %s \nTelefono: %s \nDescripcion: %s' % (cd['email'], asunto, cd['telefono'], cd['texto'])
			send_mail(asunto, content, cd['email'], ['info@duranjo.com'])
	else:
		form = contactForm()

	api = InstagramAPI(client_id='e78042ef1e834e75a28291aee734d615', client_secret='a299e7f23d0840f9b473417ea7c38c33')
	recent_media, next = api.user_recent_media(user_id="621890719", count=6)
	lista_media_url = []
	#lista_media_texto = []
	lista_media_likes = []
	lista_media_link = []
	for media in recent_media:
		lista_media_link.append(media.link)
		lista_media_url.append(media.images['standard_resolution'].url)
		#lista_media_texto.append(media.caption.text)
		lista_media_likes.append(str(media.like_count))
	zip_media = zip(lista_media_link, lista_media_url, lista_media_likes)
	ctx = {'form': form, 'success': success, 'zip_media': zip_media}
	return render_to_response('homepage/index.html', ctx, context_instance=RequestContext(request))


def works(request):
	mision = "misión de la empresa"
	vision = "visión de la empresa"
	ctx = {'mision': mision, 'vision': vision}
	return render_to_response('homepage/quienesomos.html', ctx, context_instance=RequestContext(request))


def services(request):
	serv = "El arte de servir"
	ctx = {'serv': serv}
	return render_to_response('homepage/seccionlibre.html', ctx, context_instance=RequestContext(request))


def contact(request):
	return render_to_response('homepage/contacto.html', context_instance=RequestContext(request))
