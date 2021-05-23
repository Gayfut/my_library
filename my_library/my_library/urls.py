"""my_library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from uix.views import login_view, registration_view, logout_view, main_view, profile_view, search_view, mybooks_view, book_error_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view),
    path('registration/', registration_view),
    path('profile/', profile_view),
    path('logout/', logout_view),
    path('search-result/', search_view),
    path('my-books/', mybooks_view),
    path('', main_view),
    path('book-error/', book_error_view),
]
