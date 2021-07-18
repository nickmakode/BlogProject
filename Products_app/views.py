from Products_app.models import Product
from django.shortcuts import render
from .models import Product
# Create your views here.
def products_view(request):
    prods=Product.objects.all()
    return render(request,'product_temp/product.html',{'products':prods})