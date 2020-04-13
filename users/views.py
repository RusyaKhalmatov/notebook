from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def registerUser(request):
    form = UserCreationForm()

    if request.method !='POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form': form}
    return render(request,'users/register.html',context)


def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))