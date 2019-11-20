from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import *

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

import datetime
import csv


def home(request):
    return render(request, 'ORC/home.html',
                  {'ORC': home})



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('ORC:home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def about(request):
    return render(request, 'ORC/AboutUs.html')


def workorder_list(request):
    return render(request, 'ORC/workorder_list.html')


def property_list(request):
    return render(request, 'ORC/property_list.html')


def maintenancework_list(request):
    return render(request, 'ORC/maintenancework_list.html')


def resident_list(request):
    return render(request, 'ORC/resident_list.html')


def maintenance_worker_list(request):
    return render(request, 'ORC/maintenance_worker_list.html')


def staff_list(request):
    return render(request, 'ORC/staff_list.html')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('logout')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'ORC/password_change.html', {
        'form': form
    })






