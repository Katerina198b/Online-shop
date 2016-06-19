from django.conf.urls import url, include
from product.models import Product
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [

    url(r'^(?P<pk>\d+)/$', views.ProductDetail.as_view(), name="about_product"),
    url(r'^products', views.ProductList.as_view(), name="products"),
    #url(r'^product_like/(?P<i>\d+)/$', views.ProductLikeUpdate()),
    url(r'^create/(?P<pk>\d+)', login_required(views.ProductCreate.as_view()), name='product_create'),
    url(r'^comments/(?P<pk>\d+)', views.CommentsUpdate.as_view(), name="comments"),
    url(r'^', include('core.urls', namespace="core")),

]