from django.conf.urls import url, include
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.ProductDetail.as_view(), name="about_product"),
    url(r'^products', views.ProductList.as_view(), name="products"),
    url(r'^create', login_required(views.ProductCreate.as_view()), name='product_create'),
    url(r'^', include('core.urls', namespace="core")),
]