from django.shortcuts import render, redirect
from .models import Product, CartItem
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'Comilon/home.html')

def menus(request):
    products = Product.objects.all()
    return render(request, 'Comilon/menus.html', {'products': products})

def menu_week(request):
    products = Product.objects.filter(week_special=True)
    return render(request, 'Comilon/menuweek.html', {'products': products})

def nosotros(request):
    return render(request, 'Comilon/nosotros.html')

def login_view(request):
    return render(request, 'registration/login.html')

@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'Comilon/cart.html', {'cart_items': cart_items, 'total': total})

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.delete()
    return redirect('cart')
