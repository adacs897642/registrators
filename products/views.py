from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Product

def home(request):
    products = Product.objects

    return render(request, 'products/home.html', {'products' : products})


def detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    return render(request,'products/detail.html',{'product': product})