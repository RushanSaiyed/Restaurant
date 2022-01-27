from django import forms
from .models import Member, Product

class memberform(forms.ModelForm):
    class Meta:
        model = Member 
        fields= ['username','email','phone','password']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']

class Profileform(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['username','email','phone']