from django.shortcuts import redirect, render
from django.db.models import Q
from django.http import HttpResponse
from .models import Member, Product


def login(request):
    if request.method == 'POST':
        try:
            u = request.POST['username']
            p = request.POST['password']
            print(u, p)
            x = Member.objects.get(username=u)
            if x.password == p:
                print("succes")
                return redirect('home')
            else:
                return HttpResponse("Wrong password")

        except:
            return HttpResponse("Wrong Username")

    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def home(request):
    return render(request, 'index.html')


def menu(request):
    a = Product.objects.all()
    s = request.GET.get('search')
    if s:
        q = Product.objects.filter(Q(name__icontains = s))
    else:
        q = Product.objects.all()
    #b = Product.objects.get(pk=11)
    return render(request, 'menu.html', {'abc': a, 's':q})


def orders(request):
    return render(request, 'orders.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


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

