# -*- coding: utf-8 -*-v

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls, name="admin"),
    url(r'^product/', include('product.urls', namespace="product")),
    url(r'^shop/', include('shop.urls', namespace="shop")),
    url(r'^login/', login, {'template_name': 'login.html'}, name="login"),
    url(r'^logout/', logout, {'template_name': 'logout.html', 'redirect_field_name': 'mainPage.html'}, name="logout"),
    url(r'', include('core.urls', namespace="core")),
]
