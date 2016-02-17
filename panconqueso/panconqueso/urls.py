from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.auth import views as auth_views
from django.conf import settings
from sitemaps import StaticViewSitemap
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from .apps.homepage.urls import urlpatterns as homepage_urls

sitemaps = {
	'pages': StaticViewSitemap,
}

urlpatterns = [
	# Examples:
	# url(r'^$', 'panconqueso.views.home', name='home'),
	# url(r'^panconqueso/', include('panconqueso.foo.urls')),
	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
    url(r'^admin/', admin.site.urls),
    url(r'^admin/password_reset/$', auth_views.password_reset, name='admin_password_reset'),
    url(r'^admin/password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^', include(homepage_urls)),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

if settings.DEBUG:
	from django.views.generic import TemplateView
	urlpatterns += patterns(
		'',
		url(r'^404/$', TemplateView.as_view(template_name="404.html")),
		url(r'^403/$', TemplateView.as_view(template_name="403.html")),
		(r'^500/$', TemplateView.as_view(template_name="500.html")),
		(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
	)
