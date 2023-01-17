from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.
def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    no_of_slide = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slide': no_of_slide, 'range': range(1, no_of_slide), 'products': products}
    return render(request, 'shop/index.html', params)
def aboutus(request):
    return render(request, 'shop/about.html')
def contact(request):
    return render(request, 'shop/index.html')
def tracker(request):
    return HttpResponse("tracker")
def search(request):
    return HttpResponse("search")
def productview(request):
    return HttpResponse("productview")
def checkout(request):
    return HttpResponse("checkout")
def about(request):
    return HttpResponse("about")