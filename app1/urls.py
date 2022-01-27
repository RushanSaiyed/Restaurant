from django.urls import path
from .views import add_to_cart, book_table, edit_profile, forgot_pass, home, login, about, menu, contact, orders, otpcheck, product_update, register, calculator,catwiseproduct,productview,productadd,product_delete, newpassword,logout, show_mycart

urlpatterns = [
   path('',login,name='login'),
   path('register/',register,name='register'),
   path('home/',home,name='home'),
   path('menu/',menu,name='menu'),
   path('orders/',orders,name='orders'),
   path('about/',about,name='about'),
   path('contact/',contact,name='contact'),
   path('calculator/',calculator,name='calculator'),
   path('booktable/',book_table,name='booktable'),
   path('cat/<str:name>',catwiseproduct,name='catwiseproduct'),
   path('productview/<int:pk>/',productview,name='productview'),
   path('productadd/',productadd,name='productadd'),
   path('edit/<int:pk>', product_update, name='productupdate'),
   path('delete/<int:pk>', product_delete, name='productdelete'),
   path('email/', forgot_pass, name='forgotpass'),
   path('otpcheck/',otpcheck, name = 'otpcheck'),
   path('newpassword/', newpassword, name = 'newpassword'),
   path('logout/', logout, name = 'logout'),
   path('editprofile/<int:pk>', edit_profile, name = 'editprofile'),
   path('addtocart/<int:d>', add_to_cart, name='addtocart'),   
   path('showmycart/', show_mycart, name='showmycart')
]