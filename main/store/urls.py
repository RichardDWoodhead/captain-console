
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="store_index"),
    path('product/<int:product_id>', views.product, name="product"),
    path('get_products', views.get_products),
    path('checkout/payment/', views.payment, name='payment'),
    path('checkout/review/', views.review, name='review'),
    path('checkout/confirmation/', views.confirmation, name='confirmation'),
    path('cart', views.cart, name="cart"),
    path('add_to_cart', views.add_to_cart, name='add to cart'),
    path('nav_payment', views.edit_payment, name='edit_payment'),
    path('clear_cart', views.clear_cart, name="clear_cart")
]
