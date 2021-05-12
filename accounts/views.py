from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:#given credential from user is wrong
            messages.info(request,'Invalid Credentials')
            return redirect("login")
    else:
        return render(request, 'login.html')

def register(request):

    #if we have POST request
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
                # print('Username Taken')
            elif User.objects.filter(email=email).exists():
                # print('Email Taken')
                messages.info(request,'E-mail Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('User Created')
                return redirect('login')
        else:
            # print('Password is not matching')
            messages.info(request, 'password not matching.')
            return redirect('register')
        return redirect('/')

    else: #for GET request
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')