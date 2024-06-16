from django.urls import path
from .views import add_to_cart, delete_from_cart


app_name = 'orders'


urlpatterns = [
    path('add/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('delete/<int:item_id>/', delete_from_cart, name='delete_from_cart'),
]

