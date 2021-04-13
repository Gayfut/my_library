from random import randint
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import redirect, render

from .models import User


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)

            if check_password(password, user.password):
                return render(request, "uix/main.html")
            else:
                return render(request, "uix/login.html", {"message": "Email or password is incorrect!"})
        except User.DoesNotExist:
            return render(request, "uix/login.html", {"message": "Email or password is incorrect!"})
    else:
        return render(request, "uix/login.html")


def registration_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = make_password(request.POST.get("password"))

        try:
            user = User.objects.get(email=email)
            return render(request, "uix/registration.html", {"message": "This email is used!"})
        except User.DoesNotExist:
            user = User(id=randint(1, 999999999), email=email, password=password)
        user.save()

        return redirect("/")
    else:
        return render(request, "uix/registration.html")
