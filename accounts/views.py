from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, logout

# Create your views here.
def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.get(username=request.POST["username"])
                return render(request, "accounts/signup.html", {"error":"Username has been taken."})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST["username"], password=request.POST["password1"])
                auth.login(request, user)
                return redirect("home")
        else:
            return render(request, "accounts/signup.html", {"error":"Password Mismatch."})
    else:
        return render(request, "accounts/signup.html")

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            return render(request, "accounts/login.html", {"error":"Invalid Username Or Password."})
    else:
        return render(request, "accounts/login.html")

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect("login")