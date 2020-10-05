from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', login_required(views.index), name='dashboard.index'),
    url(r'^profile/', login_required(views.profile), name='dashboard.profile'),
    url(r'^newpass/', login_required(views.newpass), name='dashboard.profile'),
    url(r'^image/', login_required(views.image), name='dashboard.profile'),

]