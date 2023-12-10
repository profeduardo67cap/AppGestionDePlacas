# from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
# from django.http import HttpResponse
# from django.db import IntegrityError

# Create your views here.

def home(request):
    return render(request,'home.html')

def logearse(request):
    if request.method == 'GET':
        return render(request,'logearse.html',{
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                    user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                    user.save()
                    login(request, user)
                    return redirect('oficina')
                    # return HttpResponse('Usuario creado satisfactoriamente')
            except:
                return render(request,'logearse.html',{
                     'form': UserCreationForm,
                     'error': 'El usuario ya existe'
                })
        return render(request,'logearse.html',{
            'form': UserCreationForm,
            'error': 'Contraseñas no coinciden'
    })

def oficina(request):
     return render(request, 'oficina.html')