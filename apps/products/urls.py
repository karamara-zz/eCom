from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name= 'products_index'),
    url(r'^(?P<product_id>\d+)/$',views.show, name='products_show'),
    url(r'^addProduct', views.create, name='products_create'),
]