"""ip2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from dbapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login$', auth_views.login, {'template_name': 'login.html'}, name="login"),
    url(r'^$', views.ip_list, name='ip_list'),
    url(r'^new$', views.ip_create, name='ip_new'),
    url(r'^edit/(?P<pk>\d+)$', views.ip_update, name='ip_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.ip_delete, name='ip_delete'),
]
