# -*- coding: utf-8 -*-v

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls, name="admin"),
    url(r'^product/', include('product.urls', namespace="product")),
    url(r'^shop/', include('shop.urls', namespace="shop")),
    # а стоит ли разрывать товар и комментарии?
    url(r'^comment/', include('comment.urls', namespace="comment")),
    url(r'^login/', login, {'template_name': 'login.html'}, name="login"),
    url(r'^logout/', logout, {'template_name': 'logout.html'}, name="logout"),
    url(r'', include('core.urls', namespace="core")),
]
