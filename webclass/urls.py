from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
	url(r'^$', 'simpleapp1.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^subs/','simpleapp1.views.subs',name='subs'),

    #user auth urls
    url(r'^accounts/login/$','simpleapp1.views.login'),
	url(r'^accounts/auth/$','simpleapp1.views.auth_view'),
    url(r'^accounts/logout/$','simpleapp1.views.logout'),
    url(r'^accounts/loggedin/$','simpleapp1.views.loggedin'),
    url(r'^accounts/invalid/$','simpleapp1.views.invalid_login'),

]
