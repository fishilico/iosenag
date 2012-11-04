from django.conf.urls import patterns, url
import mirror.views

urlpatterns = patterns('',
    url(r'^$', mirror.views.mirror, name='mirror'),
)
