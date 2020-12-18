from django import forms

class CartForm(forms.Form):
	quantity = forms.IntegerField(initial = '1')
	product_id = forms.IntegerField(widget=forms.HiddenInput)

	def __init__(self,request,*args,**kwargs):
		self.request = request
		super(CartForm,self).__init__(*args,**kwargs)