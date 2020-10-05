"""achieverz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

admin.site.site_header = "Achieverz"
admin.site.site_title = "Achieverz"
admin.site.index_title = "Achieverz Models"

urlpatterns = [
    path('adminPanel/secure/', admin.site.urls),
    url(r'^', include('home.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
]