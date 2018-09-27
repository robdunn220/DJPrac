from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ContactForm, LoginForm, RegistrationForm

def home_page(request):
    context = {
        "title":"Hello World!",
        "content":"Welcome home",
    }
    if request.user.is_authenticated:
        context["logged_in_content"] = "Yes"
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
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            print(request.user.is_authenticated)
            login(request, user)
            # context['form'] = LoginForm()
            return redirect("/")
        else:
            print("Error")
            return redirect("/register")
    return render(request, "auth/login.html", context)

def register_page(request):
    form = RegistrationForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        print(form.cleaned_data)
    return render(request, "auth/register.html", context)
