from django.urls import path
from Ecom.views import index,detail,cart_view,checkout,return_view,cancel_view

app_name ='Ecom'

urlpatterns = [
    path('', index, name ='index'),
    path('<int:product_id>/<slug:slug>', detail, name='detail'),
    path('cart/',cart_view,name='cart'),
    path('checkout/',checkout,name='checkout'),
    path('success/',return_view,name='return_view'),
    path('cancel/',cancel_view,name='cancel_view'),
]