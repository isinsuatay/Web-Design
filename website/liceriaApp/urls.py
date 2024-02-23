
from django.urls import path
from .views import HomePage
from . import views


urlpatterns = [
    path('', HomePage, name='HomePage'),
    path('contact/',views.contact,name='contact'),
    path('help/',views.help,name='help'),
    path('cart/', views.view_cart, name='cart'), 
    path('add-to-cart/',views.add_to_cart, name='add-to-cart'),
    path('checkout/', views.checkout, name='checkout'),  
    path('order_confirmation/', views.order_confirmation, name='order_confirmation'),
    path('clear-cart/', views.clear_cart, name="clear-cart"),
    path('delete-cart-item/<int:cart_item_id>/', views.delete_cart_item, name='delete_cart_item'),
    path('change-cart-item-quantity/<int:cart_item_id>/', views.change_cart_item_quantity, name='change_cart_item_quantity'),
    path('category/<slug:category_slug>/', views.category_products, name='category_products'),
  ]




 
