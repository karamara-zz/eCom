from django.shortcuts import render, redirect
from .models import Items
import datetime
# Create your views here.
def index(request):
	allItems = Items.objects.all()
	contents = {
		'products' : allItems
	}
	return render(request, 'products/index.html', contents)
def show(request):
	return render(request, 'products/show.html')
def create(request):
	print request.POST
	item = Items.objects.create(price = request.POST['price'], productName= request.POST['productName'], brand = request.POST['brand'], created_at= datetime.datetime.now())
	item.save()
	return redirect('/products')