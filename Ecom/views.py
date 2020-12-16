from django.shortcuts import render
from django.http import HttpResponse
from Ecom.models import Product
from Ecom.forms import CartForm

# Create your views here.

def index(request):
	p=Product.objects.all()
	context = {'p':p}
	return render(request,'index.html',context)

def detail(request,product_id,slug):
	d = Product.objects.get(id = product_id)
	if request.method=='POST':
		f= CartForm(request,request.POST)
		if f.is_valid():
			request.form_data = f.cleaned_data
			add_to_cart(request)
			return HttpResponse('Added to cart')

	f=CartForm(request, initial={'product_id' : Product})
	context ={'d':d,'f':f}
	return render(request,'detail.html',context)
