from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


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
    return render(request,'ORC/AboutUs.html')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'ORC/password_change.html', {
        'form': form
    })




@login_required
def workorder_list(request):
    workorder = Workorder.objects.filter(created_date__lte=timezone.now())
    return render(request, 'ORC/workorder_list.html',
                 {'workorders': workorder})

@login_required
def workorder_new(request):
   if request.method == "POST":
       form = WorkorderForm(request.POST)
       if form.is_valid():
           newworkorder = form.save(commit=False)
           newworkorder.created_date = timezone.now()
           newworkorder.save()
           workorder = Workorder.objects.filter(created_date__lte=timezone.now())
           return render(request, 'ORC/workorder_list.html',
                         {'workorders': workorder})
   else:
       form = WorkorderForm()
       # print("Else")
   return render(request, 'ORC/workorder_new.html', {'form': form})


@login_required
def workorder_edit(request, pk):
   workorder = get_object_or_404(Workorder, pk=pk)
   if request.method == "POST":
       # update
       form = WorkorderForm(request.POST, instance=workorder)
       if form.is_valid():
           workorder = form.save(commit=False)
           workorder.updated_date = timezone.now()
           workorder.save()
           workorder = Workorder.objects.filter(created_date__lte=timezone.now())
           return render(request, 'ORC/workorder_list.html',
                         {'workorders': workorder})
   else:
        # edit
       form = WorkorderForm(instance=workorder)
   return render(request, 'ORC/workorder_edit.html', {'form': form})

@login_required
def workorder_delete(request, pk):
   workorder = get_object_or_404(Workorder, pk=pk)
   workorder.delete()
   return redirect('ORC:workorder_list')

