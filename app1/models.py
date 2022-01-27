from pyexpat import model
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    Category = models.ManyToManyField(Category)
    name = models.CharField(max_length=90)
    price = models.IntegerField()
    des=models.TextField(default='')
    images=models.ImageField(upload_to='pro_img',blank=True,default='')
    
    def __str__(self):
        return self.name



class Member(models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField(default='')
    phone=models.IntegerField(default='')
    password=models.CharField(max_length=20)
    confirmpassword=models.CharField(max_length=20,default='')
    
    
    def __str__(self):
        return self.username

class calculator(models.Model):
    first = models.IntegerField()
    second = models.IntegerField()

class Tablebooking(models.Model):
    images=models.ImageField(upload_to='pro_img',blank=True,default='')
    capacity=models.IntegerField(default='')
    status=models.BooleanField(default=False)

class Bookingdate(models.Model):
    date=models.DateTimeField()
    def __unicode__(self):
        return self.date
  
    
class Order(models.Model):
    name = models.CharField(max_length=90,default='')
    price = models.IntegerField()
    images=models.ImageField(upload_to='pro_img',blank=True,default='')
    
        
class MyCart(models.Model):
    user = models.ForeignKey(Member,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True,null=True)
    update_on = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.user.username
        
        
        
        
