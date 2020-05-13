from django.shortcuts import render

# Create your views here.

def index(request):
    """A view that display the index page"""
    return render(request, "index.hml")