from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})

def detail(request):
    return render(request, 'detail.html')