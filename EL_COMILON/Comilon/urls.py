from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menus/', views.menus, name='menus'),
    path('menuweek/', views.menuweek, name='menuweek'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('login/', views.login_view, name='login'),
    path('cart/', views.cart, name='cart'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('review/', views.review, name='review'),
]
