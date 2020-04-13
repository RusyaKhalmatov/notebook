from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name="login"),
    path('register', views.registerUser, name='register'),
    path('logout', views.log_out, name='logout')
]