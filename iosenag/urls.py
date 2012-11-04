from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
import mirror.urls


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    (r'^404', TemplateView.as_view(template_name='404.html')),
    (r'^500', TemplateView.as_view(template_name='500.html')),
    url(r'^mirror/', include(mirror.urls, namespace='mirror')),
)
