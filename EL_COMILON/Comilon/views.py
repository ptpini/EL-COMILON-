from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import MenuItem, Review

def home(request):
    return render(request, 'Comilon/home.html')

def menus(request):
    return render(request, 'Comilon/menus.html')

def menuweek(request):
    return render(request, 'Comilon/menuweek.html')

def nosotros(request):
    return render(request, 'Comilon/nosotros.html')

def cart(request):
    return render(request, 'Comilon/cart.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'Comilon/login.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(
            f'Mensaje de {name} ({email})',
            message,
            settings.EMAIL_HOST_USER,
            ['your_email@example.com'],  # Reemplaza con tu dirección de correo
            fail_silently=False,
        )
        messages.success(request, 'Mensaje enviado con éxito.')
        return redirect('contact')
    return render(request, 'Comilon/contact.html')

def search(request):
    query = request.GET.get('query')
    results = MenuItem.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'Comilon/search_results.html', {'results': results, 'query': query})

def review(request):
    if request.method == 'POST':
        rating = request.POST['rating']
        comment = request.POST['comment']
        review = Review(rating=rating, comment=comment)
        review.save()
        messages.success(request, 'Reseña enviada con éxito.')
        return redirect('review')
    return render(request, 'Comilon/review.html')
