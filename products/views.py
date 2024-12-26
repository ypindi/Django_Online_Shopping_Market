from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.

# /products -> index
# URL - Uniform Resource Locator
def index(request):
    products = Product.objects.all()
    # returns all the products
    # Product.objects.filter()
    # # returns only products greater than 2 euros eg.
    # Product.objects.get()
    # # to get a single product
    # Product.objects.save()
    # # to insert a new product / update an existing one.

    # return HttpResponse('Hello World')
    # return render(request, 'index.html')
    # gives only the HTML file of index.html
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('New Page')