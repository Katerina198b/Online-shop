# -*- coding: utf-8 -*-v

from django.shortcuts import render, resolve_url
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView, ListView, CreateView
from .models import Shop
from shop.models import Shop
from forms import *


class ShopCreate(CreateView):
    model = Shop
    template_name = "createShop.html"
    fields = ('title', 'text')

    def get_success_url(self):
        return resolve_url('shop:about_shop', pk=self.object.pk)

    # в этом методе сохраняется модель
    def form_valid(self, form):
        # в этот метод поступает форма
        # form.instance.author = self.request.user
        return super(ShopCreate, self).form_valid(form)


class ShopDetail(DetailView):
    model = Shop
    template_name = "aboutShop.html"


class ShopList(ListView):
    model = Shop
    template_name = "shops.html"

    def get_queryset(self):

        queryset = Shop.objects.all()
        if self.form.cleaned_data.get('search'):
            queryset = queryset.filter(name__icontains=self.form.cleaned_data['search'])
        return queryset

    def dispatch(self, request, *args, **kwargs):
        self.form = ShopListForm(request.GET)
        self.form.is_valid()  # соответствуют ли данные введенные пользователем формочке
        # self.sort_field = request.GET.get('sort_field')
        # self.search = request.GET.get('search')
        return super(ShopList, self).dispatch(request, *args,
                                                 **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ShopList, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context
