from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from iosenag import settings
import mirror.urls
import search.urls

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    (r'^404', TemplateView.as_view(template_name='404.html')),
    (r'^500', TemplateView.as_view(template_name='500.html')),
    (r'^mirror/', include(mirror.urls, namespace='mirror')),
    (r'^search/', include(search.urls, namespace='search')),
)

# Only enable the admin in development mode, not in production
if settings.DEBUG:
    from django.contrib import admin
    admin.autodiscover()
    urlpatterns.append(url(r'^admin/', include(admin.site.urls)))
