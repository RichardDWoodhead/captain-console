
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('product/<int:product_id>', views.product, name="product"),
    path('get_products', views.get_products),
    path('checkout/payment/', views.payment, name='payment'),
    path('checkout/review/', views.review, name='review'),
    path('checkout/confirmation/', views.confirmation, name='confirmation'),
]
