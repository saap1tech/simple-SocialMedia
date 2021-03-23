from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CreateUser

# Create your views here.


def register(request):
    if request.user.is_authenticated:
        return redirect('/profile/')
    else:
        if request.method == 'POST':
            FormRegister = CreateUser(request.POST)
            if FormRegister.is_valid():
                FormRegister.save()

                username = FormRegister.cleaned_data.get('username')
                password = FormRegister.cleaned_data.get('password1')

                user = authenticate(username=username, password=password)
                login(request, user)

                return redirect('/profile/')
        else:
            FormRegister = CreateUser()

    context = {
        "form": FormRegister
    }

    return render(request, 'register.html', context)

def log_in(request):
    if request.user.is_authenticated:
        return redirect('/profile/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            if username and password:
                user = authenticate(request, username=username, password=password)

                login(request, user)

                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('/profile/')

        return render(request, 'login.html')

@login_required(login_url='/login/')
def log_out(request):
    logout(request)
    return redirect('/login/')