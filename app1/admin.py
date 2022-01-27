from django.contrib import admin
from django.shortcuts import render
from .models import MyCart, Order, Product,Category,Member,Tablebooking,Bookingdate
from django.contrib.auth.models import Group,User

admin.site.unregister(Group)
admin.site.unregister(User)


class cartfilter(admin.ModelAdmin):
    list_display = ['user','product','status','added_on']
    list_filter=['user','product','status','added_on']

    

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Member)
admin.site.register(Tablebooking)
admin.site.register(Bookingdate)
admin.site.register(Order)
admin.site.register(MyCart,cartfilter)


admin.site.site_header = "SAIYED | RESTRO"
# admin.site.site_title = "SAIYED | RESTRO - ADMIN"
# admin.site.index_title = "Welcome to SAIYED | RESTRO"
