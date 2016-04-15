from django.conf.urls import url, include
from product.models import Product
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [

    url(r'^(?P<pk>\d+)/$', views.ProductDetail.as_view(), name="about_product"),
    url(r'^products', views.ProductList.as_view(), name="products"),
    #url(r'^product_like/(?P<i>\d+)/$', views.ProductLikeUpdate()),
    url(r'^create/(?P<pk>\d+)', login_required(views.ProductCreate.as_view()), name='product_create'),
    url(r'^update/(?P<pk>\d+)', views.ProductUpdate.as_view(), name="update"),
    url(r'^comments/(?P<pk>\d+)', views.CommentsUpdate.as_view(), name="comments"),
    url(r'^dislike/(?P<pk>\d+)', views.productDislike, name="dislike"),
    url(r'^like/(?P<pk>\d+)', views.productLike, name="like"),
    url(r'^', include('core.urls', namespace="core")),

]