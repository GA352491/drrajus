from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserAdminCreationForm
from elearning.models import *
from .forms import *

from .models import *
import datetime
from datetime import date


# Create your views here.

def registerpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:

        form = UserAdminCreationForm()

        if request.method == 'POST':
            form = UserAdminCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                email = form.cleaned_data.get('email')
                user.email = email.lower()
                user.save()
                print(user)
                # form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

        context = {'form': form}
        return render(request, 'register.html', context)


def loginpage(request):
    if request.user.is_authenticated:
        # pay = Payment.objects.filter(user_name=request.user) & Payment.objects.filter(paid=True)
        # a = pay.values('paid')
        # lis = []
        # for data in a:
        #     b = lis.append(data)
        # if len(lis) >= 1:
        #     return redirect('dashboard')
        # else:
        #     return redirect('courses')
        return redirect('home')

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username.lower(), password=password)

            if user is not None:
                login(request, user)
                # pay = Payment.objects.filter(user_name=request.user) & Payment.objects.filter(paid=True)
                # a = pay.values('paid')
                # lis = []
                # for data in a:
                #     b = lis.append(data)
                # if len(lis) == 1:
                #     return redirect('dashboard')
                # else:
                #     return redirect('courses')
                return redirect('courses')
            else:
                messages.info(request, "username or password is incorrect")
                return render(request, 'login.html', )

    # form = UserAdminCreationForm()
    # if request.method == 'POST':
    #     form = UserAdminCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         user = form.cleaned_data.get('username')
    #         messages.success(request, 'Account was created for ' + user)
    #         return redirect('login')

    # context = {'form': form}
    return render(request, 'login.html', )


def logout_user(request):
    logout(request)
    return redirect('login')
