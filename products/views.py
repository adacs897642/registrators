from django.shortcuts import render

# Create your views here.
from .models import Products

def home(request):
    products = Products.objects

    return render(request, 'products/home.html', {'products' : products})
