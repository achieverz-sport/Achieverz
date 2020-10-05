from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.conf.urls import url, include
from . import views
from django.urls import path
from django.contrib import admin
login_forbidden = user_passes_test(lambda u: u.is_anonymous, 'dashboard.index', redirect_field_name=None)

urlpatterns = [
    url(r'^$', login_forbidden(views.index), name='home.index'),
    url(r'^register/$', login_forbidden(views.register),name = 'home.register'),
    url(r'^login/$',views.log_in,name = 'home.login'),
    url(r'^logout/$',views.log_out,name = 'home.logout'),
    url(r'^forgetpass/$',views.forget,name = 'home.forgetpass'),
    url(r'^about/$',views.about,name = 'home.about'),
    path('verify/<str:key>', views.verify,name="home.verify"),
    path('changepass/<str:key>', views.change_pass,name="home.change"),
    # url(r'^about/$', login_required(views.about), name='home.about'),
    url(r'^admin-login/home/user/login-as/(?P<uid>[0-9a-zA-Z]+)/$', login_required(views.loginas), name='admin.loginas'),
]