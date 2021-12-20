from django.urls import path
from .views import home, login, about, menu, contact, orders, register, calculator



urlpatterns = [
   path('',login,name='login'),
   path('register/',register,name='register'),
   path('home/',home,name='home'),
   path('menu/',menu,name='menu'),
   path('orders/',orders,name='orders'),
   path('about/',about,name='about'),
   path('contact/',contact,name='contact'),
   path('calculator/',calculator,name='calculator'),
   
]
