from django.conf.urls import patterns, url
from .views import works, index, services

urlpatterns = [
	url(r'^$', index, name="homepageindex"),
	url(r'^trabajos/$', works, name="homepageworks"),
	url(r'^servicios/$', services, name="homepageservices"),
	#url(r'^contacto/$', 'contact', name="homepagecontact"),
]
