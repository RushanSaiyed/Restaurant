from django.contrib import admin
from .models import Product,Category,Member


# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Member)

admin.site.site_header = "SAIYED | RESTRO"
admin.site.site_title = "SAIYED | RESTRO - ADMIN"
admin.site.index_title = "Welcome to SAIYED | RESTRO"
