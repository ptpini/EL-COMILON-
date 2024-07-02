from django.contrib import admin
from django.urls import path
from Comilon import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
    path('menus/', views.menus, name='menus'),
    path('menuweek/', views.menu_week, name='menuweek'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('login/', auth_views.LoginView.as_view(template_name='Comilon/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
