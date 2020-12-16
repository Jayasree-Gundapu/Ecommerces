from django.urls import path
from Ecom.views import index,detail

app_name ='Ecom'

urlpatterns = [
    path('', index, name ='index'),
    path('<int:product_id>/<slug:slug>', detail, name='detail')
]