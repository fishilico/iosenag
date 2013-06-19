from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
import iosenag.mirror.urls
import iosenag.search.urls

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    ('^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    (r'^404/?$', TemplateView.as_view(template_name='404.html')),
    (r'^500/?$', TemplateView.as_view(template_name='500.html')),
    (r'^mirror/', include(iosenag.mirror.urls, namespace='mirror')),
    (r'^search/', include(iosenag.search.urls, namespace='search')),
)

# Only enable admin urls if admin app is loaded
if 'django.contrib.admin' in settings.INSTALLED_APPS:
    from django.contrib import admin
    admin.autodiscover()
    urlpatterns.append(url(r'^admin/', include(admin.site.urls)))
