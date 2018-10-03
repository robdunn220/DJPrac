from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ContactForm, LoginForm, RegistrationForm

# Renders the information on the home page
def home_page(request):
    context = {
        "title":"Simply Morgan",
        "content":"Welcome home",
    }
    if request.user.is_authenticated:
        context["logged_in_content"] = "Yes"
    return render(request, "home_page.html", context)

# Renders the information on the about page
def about_page(request):
    context = {
        "title":"About",
        "content":"Dis About"
    }
    return render(request, "about/views.html", context)

# Renders the information on the contact page
def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title":"Contact",
        "content":"Who dis?",
        "form": contact_form
    }
    # Validates form information was entered correctly
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "contact/views.html", context)

# Renders the information on the login page
def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print("User logged in?")
    # Validates form information was entered correctly
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        # If user exists, user is validated and is sent home. Else, redirect to registration
        if user is not None:
            print(request.user.is_authenticated)
            login(request, user)
            # context['form'] = LoginForm()
            return redirect("/")
        else:
            print("Error")
            return redirect("/register")
    return render(request, "auth/login.html", context)

# Renders the information on the registration page
User = get_user_model()
def register_page(request):
    form = RegistrationForm(request.POST or None)
    context = {
        "form": form
    }
    # Validates form information is correct.
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        return redirect("/login")
    return render(request, "auth/register.html", context)
