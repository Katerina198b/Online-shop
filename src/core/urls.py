from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.getMaimPage, name="main_page"),
    url(r'^register/', views.RegisterFormView.as_view(), name="register"),
    url(r'^', views.getErrorPage, name="error_page"),
]