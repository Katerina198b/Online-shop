# -*- coding: utf-8 -*-v

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from likes import views

urlpatterns = [
    url(r'^productLike/(?P<pk>\d+)', login_required(views.productLike), name="productLike"),
    url(r'^commentLike/(?P<pk>\d+)', login_required(views.commentLike), name="commentLike"),
    url(r'^productDislike/(?P<pk>\d+)', login_required(views.productDislike), name="productDislike"),
    url(r'^commentDislike/(?P<pk>\d+)', login_required(views.commentDislike), name="commentDislike"),

]