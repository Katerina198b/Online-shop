'''from django.conf.urls import url, include
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [

    url(r'$', views.ProductDetail.as_view(), name="about_product"),
    url(r'^products', views.ProductList.as_view(), name="products"),
    #url(r'^product_like/(?P<i>\d+)/$', views.ProductLikeUpdate()),
    url(r'^create/(?P<pk>\d+)', login_required(views.ProductCreate.as_view()), name='product_create'),
    url(r'^comments/(?P<pk>\d+)', views.CommentsUpdate.as_view(), name="comments"),
    url(r'^', include('core.urls', namespace="core")),

]'''

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^comments/(?P<pk>\d+)', views.CommentsUpdate.as_view(), name="comments"),
    url(r'', views.CommentCreate.as_view(), name="about_product"),
]