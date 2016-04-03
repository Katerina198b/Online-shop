# -*- coding: utf-8 -*-v

from django.shortcuts import render, resolve_url
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView, ListView, CreateView
from .models import Shop
from comment.models import Comment
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
        # if self.search:
        #    queryset = queryset.filter(title__icontains=self.search) # почему я не могу делать сначала выбборку?
        if self.form.cleaned_data.get('search'):
            queryset = queryset.filter(title__icontains=self.form.cleaned_data['search'])
        # if self.sort_field:
        #    queryset = queryset.order_by(self.sort_field)[:10]
        if self.form.cleaned_data.get('sort_field'):
            queryset = queryset.order_by(self.form.cleaned_data['sort_field'])[:10]
        # queryset = queryset.filter(author=self.request.user)
        return queryset

    def dispatch(self, request, *args, **kwargs):  # вызывается при любом запросе к списку обтектов
        self.form = ShopListForm(request.GET)
        self.pform = ShopForm(request.POST or None)
        self.form.is_valid()  # соответствуют ли данные введенные пользователем формочке
        # self.sort_field = request.GET.get('sort_field')
        # self.search = request.GET.get('search')
        return super(ShopList, self).dispatch(request, *args,
                                                 **kwargs)  # super - вызов родительского класса с тем же именем
        ''' вызывается у класса basedView (конкретно у ListView)
        который составляет тот самый словарик отправляющийся в шаблон
        '''

    def get_context_data(self, **kwargs):
        context = super(ShopList, self).get_context_data(**kwargs)
        context['form'] = self.form
        context['pform'] = self.pform
        return context
