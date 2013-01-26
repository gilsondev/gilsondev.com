from django.conf.urls import patterns,  url

urlpatterns = patterns('gilsondev.core.views',
    url(r'^$', 'home', name='home'),
)
