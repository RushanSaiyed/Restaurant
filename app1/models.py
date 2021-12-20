from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    # price = models.IntegerField()
    def __str__(self):
        return self.name

class Product(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=90)
    price = models.IntegerField(max_length=90)
    des=models.TextField(default='')
    images=models.ImageField(upload_to='pro_img',blank=True,default='')

class Member(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=19)

class calculator(models.Model):
    first = models.IntegerField()
    second = models.IntegerField()


def __str__(self):
    return self.name
        
