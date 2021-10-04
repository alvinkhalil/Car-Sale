from django import db
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout



# Create your views here.

def login_user(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username = username, password = password)
        
        if user is not None:
            login(request,user)
            messages.info(request,"İstifadəçi adı və ya şifrə yalnışdır")
            return redirect("accounts:login")
        
        else:
            messages.success(request, "Giriş uğurla baş verdi.")
            return redirect("accounts:dashboard")


    return render(request, "accounts/login.html")

def register(request):
    
    
    if request.method == "POST":

        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"] 

        if password != confirm_password:

            messages.info(request, "Şifrələr eyni deyil")

            return redirect('accounts:register')

        else: 

            if User.objects.filter(username = username).exists():
                messages.info(request, "Bu istifadəçi artıq mövcuddur.")

                return redirect("accounts:register")
            
            else:
                if User.objects.filter(email = email).exists():

                    messages.info(request, "Bu emaildən artıq mövcuddur")

                    return redirect("accounts:register")

                else:

                    newUser = User.objects.create_user(first_name = firstname, last_name = lastname, username = username, email = email, password = password)

                    messages.success(request, "Qeydiyyatdan uğurla keçildi.")
                    login(request,newUser)
                    newUser.save()

                    return redirect("accounts:dashboard")


    return render(request, "accounts/register.html")

def logout_user(request):

    logout(request)
    messages.success(request,"Hesabınızdan uğurla çıxış edildi.")

    return redirect("pages:home")

def dashboard(request):
    
    return render(request, "accounts/dashboard.html")