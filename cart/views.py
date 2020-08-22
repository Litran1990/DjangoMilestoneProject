from django.shortcuts import render, redirect, reverse
from django.contrib import messages

# Create your views here.

def view_cart(request):
    """A View that renders the cart contents page"""
    cart = request.session.get('cart', {})
    if cart == {}:
        messages.error(request, "There are no products in the shopping cart!")
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add the selected product to the cart"""

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, 1)

    request.session['cart'] = cart
    return redirect(reverse('index'))


def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    print(request.POST)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart

    return redirect(reverse('view_cart'))