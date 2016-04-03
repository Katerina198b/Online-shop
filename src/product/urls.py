from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.ProductDetail.as_view(), name="about_product"),
    url(r'^products', views.ProductList.as_view(), name="products"),
    url(r'^product_create', views.ProductCreate.as_view(), name='product_create'),
    url(r'^', include('core.urls', namespace="core")),
]