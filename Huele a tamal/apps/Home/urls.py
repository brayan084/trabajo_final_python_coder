from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", LoginView.as_view(template_name="Home/login.html"), name="login"),
    path("about/", views.about, name="about"),
    path("register/", views.register, name="register"),
    path("logout/", LogoutView.as_view(template_name="Home/logout.html"), name="logout"),
] + staticfiles_urlpatterns()