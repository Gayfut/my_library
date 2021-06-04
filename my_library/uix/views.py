from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import redirect, render

from parser_books.parser.parser import Parser
from parser_books.parser.books_info_control import save_info, load_info
from parser_books.models import Book


def login_view(request):
    """view for login page"""
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
    """view for registration page"""
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
    """view for logout"""
    logout(request)

    return redirect("/")


@login_required(login_url='/login')
def main_view(request):
    """view for main page with search function"""
    username = request.user.username

    if request.method == "POST":
        search_query = request.POST.get("search")

        parser = Parser()

        books_info1 = parser.start_parse(search_query, 1)
        save_info(books_info1, 1, username)

        books_info2 = parser.start_parse(search_query, 2)
        save_info(books_info2, 2, username)

        books_info3 = parser.start_parse(search_query, 3)
        save_info(books_info3, 3, username)

        parser.stop_parse()

        return redirect("/search-result/")

    return render(request, "uix/main.html", {"username": username})


@login_required(login_url='/login')
def profile_view(request):
    """view for user profile page"""
    username = request.user.username
    email = request.user.email

    return render(request, "uix/profile.html", {"username": username, "email": email})


@login_required(login_url='/login')
def search_view(request):
    """view for search result page"""
    username = request.user.username

    books_info1 = load_info(1, username)
    books_info2 = load_info(2, username)
    books_info3 = load_info(3, username)

    if request.method == "POST":
        book_link = request.POST.get("add")
        for book in books_info1+books_info2+books_info3:
            if book_link == book["link"]:
                user_id = request.user.id
                try:
                    book_for_save = Book.objects.get(link=book["link"])
                except Book.DoesNotExist:
                    book_for_save = Book(link=book["link"])
                book_for_save.name = book["name"]
                book_for_save.author = book["author"]
                book_for_save.description = book["description"]
                book_for_save.img_link = book["img_link"]
                book_for_save.download_link = book["download_link"]
                book_for_save.save()

                user = User.objects.get(pk=user_id)
                user.profile.books.add(book_for_save)
                user.save()

    return render(request, "uix/search-result.html", {"username": username, "books_info1": books_info1, "books_info2": books_info2, "books_info3": books_info3})


def get_books_info(user):
    """return user books"""
    books_id_dict = user.profile.books.values('id')
    books_id = []

    for book_id in books_id_dict:
        books_id.append(book_id["id"])

    books_info = []
    for book_id in books_id:
        book = Book.objects.filter(id=book_id).first()
        books_info.append(book)

    return books_info


@login_required(login_url='/login')
def mybooks_view(request):
    """view for my-books page"""
    username = request.user.username

    user_id = request.user.id
    user = User.objects.get(pk=user_id)

    if request.method == "POST":
        book_id = request.POST.get("delete")

        user.profile.books.filter(id=book_id).first().delete()

        return render(request, "uix/my-books.html", {"username": username, "books_info": get_books_info(user)})

    return render(request, "uix/my-books.html", {"username": username, "books_info": get_books_info(user)})


@login_required(login_url='/login')
def book_error_view(request):
    """view for book download link error"""
    username = request.user.username

    return render(request, "uix/book-error.html", {"username": username})
