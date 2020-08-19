from django.shortcuts import render
from products.models import Product

# Create your views here.

def index(request):
    """A view that display the index page"""
    index = Product.objects.all()
    return render(request, "index.hml", {"index": index})