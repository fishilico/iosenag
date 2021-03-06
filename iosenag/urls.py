from django.conf import settings
from django.conf.urls import include, url
from django.views.generic import RedirectView, TemplateView
import iosenag.mirror.urls
import iosenag.search.urls

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'icons/favicon.ico')),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    url(r'^404/?$', TemplateView.as_view(template_name='404.html')),
    url(r'^500/?$', TemplateView.as_view(template_name='500.html')),
    url(r'^mirror/', include(iosenag.mirror.urls, namespace='mirror')),
    url(r'^search/', include(iosenag.search.urls, namespace='search')),
]

# Only enable admin urls if admin app is loaded
if 'django.contrib.admin' in settings.INSTALLED_APPS:
    from django.contrib import admin
    admin.autodiscover()
    urlpatterns.append(url(r'^admin/', include(admin.site.urls)))
