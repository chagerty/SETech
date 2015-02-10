from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'SETechExcercise.views.home', name='home'),
)
