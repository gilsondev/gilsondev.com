from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'', include('pages.urls', namespace='site')),
    url(r'', include('contact.urls', namespace='contact'))
)
