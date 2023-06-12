from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def index(request: HttpResponse) -> HttpResponse:
    return render(request, 'Home/index.html')    

def about(request: HttpResponse) -> HttpResponse:
    return render(request, 'Home/about.html')

@staff_member_required
def register(request: HttpResponse) -> HttpResponse:
    if request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "Home/index.html", )
    else:
        form = forms.CustomUserCreationForm()
    return render(request, "Home/register.html", {"form": form})