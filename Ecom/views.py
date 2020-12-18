from django.shortcuts import render,redirect
from django.http import HttpResponse
from Ecom.models import Product,Buy
from Ecom.forms import CartForm
from Ecom.myapp import *
from django.urls import reverse
from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm

# Create your views here.

def index(request):
	p=Product.objects.all()
	if request.GET.get('q'):
		query = request.GET.get('q')
		p=Product.objects.filter(title__contains=query)
	context = {'p':p}
	return render(request,'index.html',context)

def detail(request,product_id,slug):
	d = Product.objects.get(id = product_id)

	if request.method == 'POST':
		f =CartForm(request,request.POST)
		if f.is_valid():
			request.form_data = f.cleaned_data
			add_to_cart(request)
			return redirect('Ecom:cart')

	f=CartForm(request, initial={'product_id' : product_id})
	context ={'d':d,'f':f}
	return render(request,'detail.html',context)

def cart_view(request):
	if request.method == 'POST' and request.POST.get('delete') == 'Delete':
		item_id = request.POST.get('item_id')
		cd = Cart.objects.get(id= item_id)
		cd.delete()
	c = get_cart(request)
	t = total_(request)
	context = {'c':c,'t':t}       
	return render(request,'cart.html',context)


def checkout(request):
	items=get_cart(request)
	for i in items:
		b=Buy(product_id=i.product_id,quantity=i.quantity,price=i.price)
		b.save()

	paypal_dict = {
	"business": "sb-4uv0434137187@business.example.com",
	"amount": total_(request),
	"item_name": cart_id_(request),
	"invoice": cart_id_(request),
	"notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
	"return": request.build_absolute_uri(reverse('Ecom:return_view')),
	"cancel_return": request.build_absolute_uri(reverse('Ecom:cancel_view')),
	"custom": "premium_plan",
	}
	form = PayPalPaymentsForm(initial=paypal_dict)
	context = {"form": form,"items":items,"total":total_(request)}
	return render(request, "checkout.html", context)

def return_view(request):
	return HttpResponse('Transaction Successful')

def cancel_view(request):
	return HttpResponse('Transaction Cancelled !')


