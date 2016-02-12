from django.contrib import admin

#for uploading stuff
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', 'simpleapp1.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^subs/','simpleapp1.views.subs',name='subs'),
    url(r'^videolist/','simpleapp1.views.video_list'),
    #user auth urls
    # url(r'^accounts/login/','simpleapp1.views.login'),
	url(r'^accounts/auth/','simpleapp1.views.auth_view'),
    url(r'^accounts/logout/','simpleapp1.views.logout'),
    url(r'^accounts/loggedin/','simpleapp1.views.loggedin'),
    url(r'^accounts/invalid/','simpleapp1.views.invalid_login'),
    url(r'^accounts/register/$','simpleapp1.views.register_user'),
    url(r'^accounts/register_success/','simpleapp1.views.register_success'),
    url(r'^upload/','simpleapp1.views.upload'),
    url(r'^upload_pic/','simpleapp1.views.upload_pic'),
]
