from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def index(request):
    products = Product.objects.all()  # This method calls
    # all prods in db
    return render(request, 'index.html',
                  {'products': products})  # This injects
    # the data from products in index.html template


def new_prods(request):
    return HttpResponse('Here goes my new products')

