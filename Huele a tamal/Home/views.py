from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.

def index(request: HttpResponse) -> HttpResponse:
    return render(request, 'Home/index.html')    

def register(request: HttpResponse) -> HttpResponse:
    if request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "Home/index.html", {"message": "User created"})
    else:
        form = forms.CustomUserCreationForm()
    return render(request, "Home/register.html", {"form": form})