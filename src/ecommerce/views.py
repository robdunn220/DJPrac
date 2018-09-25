from django.shortcuts import render
from django.http import HttpResponse

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
    context = {
        "title":"Contact",
        "content":"Who dis?"
    }
    if request.method == "POST":
        print(request.POST)
    return render(request, "contact/views.html", context)
