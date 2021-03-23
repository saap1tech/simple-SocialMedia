from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from .models import Chat


@login_required(login_url='/login/')
def home(request):
    rooms = User.objects.exclude(username=request.user)

    context = {
        'rooms': rooms,
    }

    return render(request, 'home.html', context)

@login_required(login_url='/login/')
def index(request, rec):

    request.session['rec'] = rec

    rooms = User.objects.exclude(username=request.user)

    context = {
        'receiver': rec,
        'rooms': rooms,
    }

    return render(request, 'indexc.html', context)

def send(request):
    message = request.POST.get('message')
    receiver = request.POST.get('receiver')

    try:
        Chat.objects.create(sender=request.user, receiver=receiver, msg=message)

        resp = {
            "status": "success"
        }

    except Exception as e:
        resp = {
            "status": f"failed and the error is {e}"
        }

    return JsonResponse(resp)

def show(request):
    filter1 = Chat.objects.filter(sender=request.user, receiver=request.session['rec'])
    filter2 = Chat.objects.filter(sender=request.session['rec'], receiver=request.user)

    context = {
        "data": filter1 | filter2
    }

    return render(request, 'show.html', context)