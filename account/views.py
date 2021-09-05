from django.shortcuts import render, redirect
from django.contrib import  messages
from . models import *
from django.contrib.auth.models import auth
# Create your views here.
def login(request):
    if request.method=="POST":
        try:
            userdetais=ash.objects.get(username=request.POST['username'],password1=request.POST['psw'])
            request.session['username']=userdetais.username
            return redirect('home')
        except ash.DoesNotExist:
            messages.success(request,'invalid usernme and password')
        return render(request, 'login.html')


    return render(request,'login.html')
def regi(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if ash.objects.filter(username=username).exists():
                messages.info(request,'username already taken')
                return redirect('reg')
            elif ash.objects.filter(email=email).exists():
                messages.info(request,'email already taken')
                return redirect('reg')
            else:
                use=ash.objects.create(username=username,firstname=firstname,email=email,password1=password1)
                use.save()
            return redirect('log')
        else:
            messages.info(request,'password does not mach ')
            return redirect('reg')

    else:

        return render(request,'register.html')
def logout(request):
    try:
        del request.session['username']
    except:
        return redirect('/')
    return redirect('/')