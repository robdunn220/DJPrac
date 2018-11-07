from django.conf.urls import url
app_name = 'ecommerce'

from .views import (
    ProductListView,
    ProductDetailSlugView,
)

# Initializes URL's
urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
]
