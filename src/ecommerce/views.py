from django.shortcuts import render
from django.http import HttpResponse

from .forms import ContactForm, LoginForm

def home_page(request):
    context = {
    "title":"Hello World!",
    "content":"Welcome home"
    }
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "title":"About",
        "content":"Dis About"
    }
    return render(request, "about/views.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title":"Contact",
        "content":"Who dis?",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "contact/views.html", context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print("User logged in?")
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "auth/login.html", context)

def register_page(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "auth/register.html", {})
