# -*- coding: utf-8 -*-v

from django.shortcuts import render, resolve_url
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView, ListView, CreateView
from .models import Product, Comment
from shop.models import Shop
from forms import *


class ProductCreate(CreateView):
    model = Product
    template_name = "createProduct.html"
    fields = ('name', 'description')

    def get_success_url(self):
        return resolve_url('product:about_product', pk=self.object.pk)

    # в этом методе сохраняется модель
    def form_valid(self, form):
        # в этот метод поступает форма
        # form.instance.author = self.request.user
        return super(ProductCreate, self).form_valid(form)

class CommentCreate(CreateView):
    model = Comment
    fields = ('text')

    def get_success_url(self):
        return resolve_url('product:about_product')

    def form_valid(self, form):
        return super(CommentCreate, self).form_valid(form)


class ProductDetail(DetailView):
    model = Product
    template_name = "aboutProduct.html"


class ProductList(ListView):
    model = Product
    template_name = "products.html"

    def get_queryset(self):

        queryset = Product.objects.all()
        # if self.search:
        #    queryset = queryset.filter(title__icontains=self.search) # почему я не могу делать сначала выбборку?
        if self.form.cleaned_data.get('search'):
            queryset = queryset.filter(name__icontains=self.form.cleaned_data['search'])
        # if self.sort_field:
        #    queryset = queryset.order_by(self.sort_field)[:10]
        if self.form.cleaned_data.get('sort_field'):
            queryset = queryset.order_by(self.form.cleaned_data['sort_field'])[:10]
        # queryset = queryset.filter(author=self.request.user)
        #if self.form.cleanded_data.get('quantity'):
        #    queryset = queryset[:self.form.sort_field]
        return queryset

    def dispatch(self, request, *args, **kwargs):  # вызывается при любом запросе к списку обтектов
        self.form = ProductListForm(request.GET)
        self.cform = CommentForm(request.POST or None)
        self.form.is_valid()  # соответствуют ли данные введенные пользователем формочке
        # self.sort_field = request.GET.get('sort_field')
        # self.search = request.GET.get('search')
        return super(ProductList, self).dispatch(request, *args,
                                                 **kwargs)  # super - вызов родительского класса с тем же именем
        ''' вызывается у класса basedView (конкретно у ListView)
        который составляет тот самый словарик отправляющийся в шаблон
        '''

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        context['form'] = self.form
        context['cform'] = self.cform
        return context
