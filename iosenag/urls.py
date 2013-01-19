from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
import mirror.urls
import search.urls

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    (r'^404', TemplateView.as_view(template_name='404.html')),
    (r'^500', TemplateView.as_view(template_name='500.html')),
    url(r'^mirror/', include(mirror.urls, namespace='mirror')),
    url(r'^search/', include(search.urls, namespace='search')),
    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
