from django.conf.urls import url
from django.contrib import admin
from .views import CoreViews
from . import views

urlpatterns = [
    url(r'^$', views.getMaimPage, name="main_page"),
    url(r'^', views.getErrorPage, name="error_page"),
]