# -*- coding: utf-8 -*-v

from django.shortcuts import render

from core.forms import UserCreateForm
from core.models import Core
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, resolve_url, get_object_or_404
from django.contrib import auth





def getMaimPage(request):
    return render(request, 'mainPage.html')


def getErrorPage(request):
    return render(request, 'errorPage.html')


class RegisterFormView(FormView):
    form_class = UserCreateForm
    template_name = "register.html"

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    #success_url = "core:mainPage"

    def get_success_url(self):
        return resolve_url('core:main_page')

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()
        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)

