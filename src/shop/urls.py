# -*- coding: utf-8 -*-v

from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.ShopDetail.as_view(), name="about_shop"),
    url(r'^shops', views.ShopList.as_view(), name="shops"),
    url(r'^create', login_required(views.ShopCreate.as_view()), name='shop_create'),
    url(r'^', include('core.urls', namespace="core")),
]