from django.conf.urls import patterns,  url

urlpatterns = patterns('gilsondev.portfolio.views',
    url(r'$', 'list', name='portfolios'),
)
