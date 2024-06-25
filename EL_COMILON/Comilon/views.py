from django.shortcuts import render

def home(request):
    return render(request, 'Comilon/home.html')

def menus(request):
    return render(request, 'Comilon/menus.html')

def menuweek(request):
    return render(request, 'Comilon/menuweek.html')

def nosotros(request):
    return render(request, 'Comilon/nosotros.html')

def login(request):
    return render(request, 'Comilon/login.html')

def cart(request):
    return render(request, 'Comilon/cart.html')
