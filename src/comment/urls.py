from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('core.urls', namespace="core")),
]