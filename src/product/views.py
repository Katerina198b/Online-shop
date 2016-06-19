# -*- coding: utf-8 -*-v
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, resolve_url, get_object_or_404
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from shop.models import Shop

from likes.models import Likes
from .models import Product, Comment
from django.db import models
from forms import *
from django.conf import settings
from django.shortcuts import redirect
from django.http import JsonResponse


class ProductUpdate(UpdateView):

    model = Product
    template_name = "updateProduct.html"
    fields = ('name', 'description', 'image')


    def get_success_url(self):
        return resolve_url('product:about_product', pk=self.object.pk)

class ProductCreate(CreateView):

    model = Product
    template_name = "createProduct.html"
    fields = ('name', 'description', 'image', 'publish', 'category')


    def dispatch(self, request, pk=None, *args, **kwargs):
        self.shop = get_object_or_404(Shop, id=pk)
        return super(ProductCreate, self).dispatch(request, *args, **kwargs)


    def get_success_url(self):
        return resolve_url('product:about_product', pk=self.object.pk)


    def form_valid(self, form):

        # в этот метод поступает форма
        form.instance.shop = self.shop
        form.instance.author = self.request.user
        return super(ProductCreate, self).form_valid(form)

class CommentsUpdate(DetailView):

    template_name = "updateComments.html"
    model = Product

class ProductDetail(CreateView):

    model = Comment
    template_name = "aboutProduct.html"
    fields = ('text', )

    def get_context_data(self, **kwargs):
        self.context = super(ProductDetail, self).get_context_data(**kwargs)
        self.context['product'] = self.product
        return self.context


    def dispatch(self, request, pk=None, *args, **kwargs):
        self.product = get_object_or_404(Product, id=pk)
        return super(ProductDetail, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return resolve_url('product:about_product', pk=self.product.pk)


    def form_valid(self, form):
        if not self.request.user.is_authenticated():
            return redisrect('%s?next=%s' % (settings.LOGIN_URL, self.request.path))
        form.instance.product = self.product
        form.instance.author = self.request.user
        return super(ProductDetail, self).form_valid(form)

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
        if self.form.cleaned_data.get('search_tag'):
                queryset = queryset.filter(category__in=self.form.cleaned_data['search_tag'])
        # queryset = queryset.filter(author=self.request.user)
        #if self.form.cleanded_data.get('quantity'):
        #    queryset = queryset[:self.form.sort_field]
        queryset = queryset.annotate(comment_count=models.Count('comments'))
        if self.form.cleaned_data.get('sort_field'):
            queryset = queryset.order_by(self.form.cleaned_data['sort_field'])[::-1]

        return queryset

    def dispatch(self, request, *args, **kwargs):

        # вызывается при любом запросе к списку обтектов
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
