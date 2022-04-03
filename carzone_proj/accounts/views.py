from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


# Create your views here.
def login(request):
    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.ERROR(request, 'Username already exist!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.ERROR(request, 'Email is already exist!')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                    auth.login(request, user)
                    messages.success(request, 'you are logged !')
                    return redirect('dashboard')
                    user.save()
                    messages.success(request, 'you are registered successfully!')
                    return redirect('login')

        else:
            messages.ERROR(request, 'Password do not match!')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def logout(request):
    return redirect("home")


def dashboard(request):
    return render(request, "accounts/dashboard.html")
