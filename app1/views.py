import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.http import HttpResponse, request
from .models import Bookingdate, Category, Member, MyCart, Product, Tablebooking
from .forms import OrderForm, Profileform
import smtplib, ssl
import random
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        try:
            e=request.POST['email']
            p = request.POST['password']
            print(e, p)
            x = Member.objects.get(email=e)
            if x.password == p:
                request.session['email']=e
                messages.success(request, 'Succesfully Logged In ')
                # messages.info(request, 'Welcome {e} !')
                return redirect('home')
            else:
                messages.info(request, 'Wrong Password')
        except:
            messages.info(request, 'Wrong Email')

    return render(request, 'login.html')


def register(request):
   if request.method == 'POST':
       obj = Member()
       obj.username = request.POST['username']
       obj.email = request.POST['email']
       obj.phone = request.POST['phone']
       obj.password = request.POST['password']
       print(obj.password)
       obj.confirmpassword = request.POST['confirmpassword']
       print(obj.confirmpassword)
       if obj.confirmpassword == obj.password:
           obj.save()
           messages.success(request, 'Your account have been successfully created')
       else:
           messages.info(request, 'Password does not match')
           return redirect('register')
   return render(request, 'register.html')


def home(request):
    if request.session.has_key('email'):
        # a=Product.objects.all()
        user1=request.session['email']
        print(user1)
        per=Member.objects.get(email=user1)
        print(per.username)
    return render(request, 'index.html',{'per':per})


def menu(request):
    if request.session.has_key('email'):
        user1 = request.session['email']
        per = Member.objects.get(email=user1)
        # a = Product.objects.all()
        cat = Category.objects.all()
        s = request.GET.get('search')
        if s:
            q = Product.objects.filter(Q(name__icontains = s))
        else:
            q = Product.objects.all()
        #b = Product.objects.get(pk=11)
    else:
        return redirect('login')
    return render(request, 'menu.html',{'rushan':cat,'s':q,'per':per})


def orders(request):
    if request.session.has_key('email'):
        user1 = request.session['email']
        per = Member.objects.get(email=user1)
        order = Product.objects.all()
    else:
        return redirect('login')
    return render(request,'orders.html',{'pro_list':order,'per':per})


def about(request):
    if request.session.has_key('email'):
        user1 = request.session['email']
        per = Member.objects.get(email=user1)
    else:
        return redirect('login')
    return render(request, 'about.html',{'per':per})


def contact(request):
    if request.session.has_key('email'):
        user1 = request.session['email']
        per = Member.objects.get(email=user1)
        return render(request, 'contact.html')
    else:
        return redirect('login')
    return render(request, 'contact.html',{'per':per})


def calculator(request):
    if request.GET:

        val1 = request.GET['first']
        val2 = request.GET['second']
        opt = request.GET['choice']

        if opt == 'add':
            arsh = int(val1) + int(val2)
            return render(request,'calculator.html', {'ans':arsh, 'val1':val1, 'val2':val2})
        elif opt == 'sub':
            arsh = int(val1) - int(val2)
            return render(request,'calculator.html', {'ans':arsh,'val1':val1, 'val2':val2})
        elif opt == 'mul':
            arsh = int(val1) * int(val2)
            return render(request,'calculator.html', {'ans':arsh,'val1':val1, 'val2':val2})
        elif opt == 'div':
            arsh = int(val1) / int(val2)
            return render(request,'calculator.html', {'ans':arsh,'val1':val1, 'val2':val2})
            
    return render(request, 'calculator.html')


def book_table(request):
    if request.session.has_key('email'):
        user1 = request.session['email']
        per = Member.objects.get(email=user1)
        x = Tablebooking.objects.filter(status = True)
        if request.method == 'POST':   
            obj = Bookingdate()
            obj.date = request.POST['date']
            obj.save()
    return render(request, 'book_table.html',{'xyz':x,'per':per})
        

def catwiseproduct(request,name): 
    if request.session.has_key('email'):
        user1 = request.session['email']
        per = Member.objects.get(email=user1)
        cat=Category.objects.get(name=name)
        cate = Category.objects.all()
    # print(cat)
        product=Product.objects.all().filter(Category=cat)
    # print(product)
    return render(request,'catwise.html',{'cat':cat,'rushan':cate,'pro':product,'per':per})
        
     
def productview(request, pk):
    if request.session.has_key('email'):
        user1 = request.session['email']
        per = Member.objects.get(email=user1) 
        view = get_object_or_404(Product, pk=pk)
    return render(request, 'productview.html',{'v':view, 'per':per})
    

def productadd(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('orders')
    return render(request, 'pro_form.html', {'form':form})


def edit_profile(request,pk):
    if request.session.has_key('email'):
        profile = Member.objects.get(email=request.session['email'])
        if request.method == 'POST':
            profile.username = request.POST['username'] or None
            profile.email = request.POST['email'] or None
            profile.phone = request.POST['phone'] or None
            profile.password = request.POST['password'] or None
            profile.save()
            return redirect('login')
    return render(request, 'editprofile.html',{'profile':profile})


def product_update(request,pk):
    food = get_object_or_404(Product, pk=pk)
    form = OrderForm(request.POST or None, instance=food)
    if form.is_valid():
        form.save()
        return redirect('orders')
    return render(request, 'pro_form.html',{'form':form})


def product_delete(request,pk):
    food = get_object_or_404(Product, pk=pk)
    food.delete()
    return redirect('orders')
    
        
def forgot_pass(request):
    email=request.POST.get('email')
    request.session['email']=email
    if email == None:
        return render(request,'email.html')
    print("email:",email)
    otp = ''
    ran = random.choice('0123456789')
    ran1 = random.choice('0123456789')
    ran2 = random.choice('0123456789')
    ran3 = random.choice('0123456789')

    otp = ran + ran1 + ran2 + ran3
    print("OTP : ",otp)
    # print("nnn")
    request.session['otp'] = otp

    port = 465
    password = "saiyedrestro@786"
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL("smtp.gmail.com",port,context=context)
    server.login("saiyedrestro@gmail.com",password)
    server.sendmail("{email}",email,otp)
    server.quit()

    return redirect('otpcheck')

      
def otpcheck(request):
    if request.session.has_key('otp'):
        # print("hhhh")
        otp = request.session['otp']
        try:
            otpobj = request.POST.get('otp')

            if otpobj == None:
                return render(request,'otp.html')
            if otp == request.POST.get('otp'):
                return redirect('newpassword')
            else:
                messages.info(request, 'Wrong OTP Entered')
        except:
            return redirect('login')
    
    return render(request,'otp.html')
    
    
def newpassword(request):    
    new_pass = request.POST.get('password')
    if new_pass == None:
        return render(request, 'newpassword.html')
    obj = Member.objects.get(email = request.session['email'])
    obj.password = new_pass
    obj.save()
    return redirect('login')
    

def logout(request):
    if request.session.has_key('email'):
        del request.session['email']
    return redirect('login')
        

def add_to_cart(request,d):
    if request.session.has_key('email'):
        if request.method == 'POST':
            per=Member.objects.get(email=request.session['email'])
            pro=Product.objects.get(id=d)
            
            if MyCart.objects.filter(username_id=per.pk, pro_id=pro.id, status=False).exists():
                return(HttpResponse('This Product is Already in Cart'))
            else:
                cart = MyCart()
                cart.user = per
                cart.product = pro
                cart.added_on=datetime.datetime.now()
                cart.save()
    return(redirect('addtocart',d))
    
            
def show_mycart(request):
    if request.session.has_key('email'):
        obj = Member.objects.get(email=request.session['email'])
        all = MyCart.objects.filter(user=obj.pk)
        l=[]
        p=0
        for i in all:
            l.append(i.product)
            p=p+i.product.price
    return render(request,'mycart.html',{'al':l,'obj':obj,'p':p})
        
    