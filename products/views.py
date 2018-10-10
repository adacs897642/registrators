from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Product, ProductDoc


def home(request):
    products = Product.objects

    return render(request, 'products/home.html', {'products': products})


def detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    product_docs = ProductDoc.objects.filter(product_id=product_id).order_by('-title')

    return render(request,'products/detail.html',{'product': product, 'product_docs':product_docs})