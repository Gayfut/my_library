from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import redirect, render

from parser.parser1 import Parser1
from parser.parser2 import Parser2
from parser.parser3 import Parser3


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


def logout_view(request):
    logout(request)

    return redirect("/")


@login_required(login_url='/login')
def main_view(request):
    username = request.user.username

    if request.method == "POST":
        search_query = request.POST.get("search")

        parser1 = Parser1()
        books_info1 = parser1.start_parse(search_query)
        parser1.stop_parse()

        parser2 = Parser2()
        books_info2 = parser2.start_parse(search_query)
        parser2.stop_parse()

        parser3 = Parser3()
        books_info3 = parser3.start_parse(search_query)
        parser3.stop_parse()

        return render(request, "uix/search-result.html",
                      {"username": username, "books_info1": books_info1, "books_info2": books_info2,
                       "books_info3": books_info3})

    return render(request, "uix/main.html", {"username": username})


@login_required(login_url='/login')
def profile_view(request):
    username = request.user.username
    email = request.user.email
    password = request.user.password

    return render(request, "uix/profile.html", {"username": username, "email": email, "password": password})


@login_required(login_url='/login')
def search_view(request, search_query):
    username = request.user.username

    parser1 = Parser1()
    books_info1 = parser1.start_parse(search_query)
    parser1.stop_parse()

    parser2 = Parser2()
    books_info2 = parser2.start_parse(search_query)
    parser2.stop_parse()

    parser3 = Parser3()
    books_info3 = parser3.start_parse(search_query)
    parser3.stop_parse()

    return render(request, "uix/search-result.html", {"username": username, "books_info1": books_info1, "books_info2": books_info2, "books_info3": books_info3})
