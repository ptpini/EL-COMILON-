from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import Product, CartItem
from .forms import RegisterForm

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

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'Comilon/login.html', {'error': 'Invalid credentials'})
    return render(request, 'Comilon/login.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'Comilon/register.html', {'form': form})

def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price for item in cart_items)
    return render(request, 'Comilon/cart.html', {'cart_items': cart_items, 'total': total})

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')

def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.delete()
    return redirect('cart')

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Product, CartItem

def home(request):
    return render(request, 'Comilon/home.html')

def menu(request):
    products = Product.objects.all()
    return render(request, 'Comilon/menu.html', {'products': products})

def menu_week(request):
    products = Product.objects.filter(week_special=True)
    return render(request, 'Comilon/menuweek.html', {'products': products})

def nosotros(request):
    return render(request, 'Comilon/nosotros.html')

def login_view(request):
    return render(request, 'Comilon/login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'Comilon/register.html', {'form': form})

def cart(request):
    cart_items = request.session.get('cart_items', [])
    total = sum(item['total_price'] for item in cart_items)
    return render(request, 'Comilon/cart.html', {'cart_items': cart_items, 'total': total})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_items = request.session.get('cart_items', [])
    for item in cart_items:
        if item['product_id'] == product_id:
            item['quantity'] += 1
            item['total_price'] = item['quantity'] * product.price
            break
    else:
        cart_items.append({
            'product_id': product.id,
            'name': product.name,
            'price': product.price,
            'quantity': 1,
            'total_price': product.price,
        })
    request.session['cart_items'] = cart_items
    return redirect('cart')

def remove_from_cart(request, cart_item_id):
    cart_items = request.session.get('cart_items', [])
    cart_items = [item for item in cart_items if item['product_id'] != cart_item_id]
    request.session['cart_items'] = cart_items
    return JsonResponse({'success': True})
