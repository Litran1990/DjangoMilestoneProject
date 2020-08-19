from django.conf.urls import url, include
from .views import all_products, home

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^all_products', all_products, name='products')
]