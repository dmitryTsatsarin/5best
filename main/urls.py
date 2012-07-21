from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', "main.views.index", name="index"),
    url(r'^dashboard/$', "main.views.dashboard", name="dashboard"),
    url(r'^profile/(?P<id>\d+)/$', "main.views.profile", name="profile"),
    url(r'^group/(?P<id>\d+)/$', "main.views.group", name="group"),
)
