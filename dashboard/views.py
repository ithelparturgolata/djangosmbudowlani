from django.shortcuts import render, redirect, HttpResponse
from dashboard.forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# homepage view
def home(request):
    return render(request, ("dashboard.html"))


# register view
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"form": form}
    return render(request, "register.html", context=context)


# login view
def login_view(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, "Zalogowano")

                return redirect("dashboard")

    context = {"form": form}
    return render(request, "login.html", context=context)


# logout view
def logout_view(request):
    auth.logout(request)
    messages.success(request, "Wylogowano")
    return redirect("login")


@login_required(login_url="login")
def dashboard(request):
    return render(request, "dashboard.html")


def dashboard_main(request):
    return render(request, "dashboard.html")


def iso_iso(request):
    return render(request, "iso-iso.html")

def iso_polityka(request):
    return render(request, "iso-polityka.html")

def iso_badanie(request):
    return render(request, "iso-badanie.html")

def wspolnoty(request):
    return render(request, "wspolnoty.html")


def kontakt(request):
    return render(request, "kontakt.html")


def spoldzielnia_organy(request):
    return render(request, "spoldzielnia-organy.html")