from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import redirect, render


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)

            if check_password(password, user.password):
                login(request, user)

                return redirect("/")
            else:
                return render(request, "uix/login.html", {"message": "Email or password is incorrect!"})
        except User.DoesNotExist:
            return render(request, "uix/login.html", {"message": "Email or password is incorrect!"})
    else:
        return render(request, "uix/login.html")


def registration_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = make_password(request.POST.get("password"))

        try:
            user = User.objects.get(email=email)

            return render(request, "uix/registration.html", {"message": "This email is used!"})
        except User.DoesNotExist:
            user = User(username=username, email=email, password=password)
        user.save()

        return redirect("/")
    else:
        return render(request, "uix/registration.html")


@login_required(login_url='/login')
def main_view(request):
    return render(request, "uix/main.html")
