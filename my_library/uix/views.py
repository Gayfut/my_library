from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = "uix/login.html"


class RegistrationView(TemplateView):
    template_name = "uix/registration.html"
