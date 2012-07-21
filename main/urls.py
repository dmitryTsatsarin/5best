from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', "main.views.index", name="index"),
    url(r'^dashboard/$', "main.views.dashboard", name="dashboard"),
    url(r'^profile/(?P<id>\d+)/$', "main.views.profile", name="profile"),
    url(r'^groups/$', "main.views.groups", name="groups"),
    url(r'^group/(?P<id>\d+)/$', "main.views.group", name="group"),

    url(r'^account/login/$', "main.views.login", name="account_login"),
    url(r'^account/logout/$', "main.views.logout", name="account_logout"),
)
