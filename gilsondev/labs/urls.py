from django.conf.urls import patterns,  url

urlpatterns = patterns('gilsondev.labs.views',
    url(r'$', 'list', name='projects'),
)
