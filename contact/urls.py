from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from .views import ContactView

urlpatterns = patterns('',
    url('^contato/$', ContactView.as_view(), name='contact'),
    url('^contato/enviado/$', TemplateView.as_view(
        template_name='contact/success.html'), name='success'),
)
