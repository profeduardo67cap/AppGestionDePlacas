# from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# from django.http import HttpResponse
# from django.db import IntegrityError

# Create your views here.

def home(request):
    return render(request,'home.html')

def loguearse(request):
    if request.method == 'GET':
        return render(request,'loguearse.html',{
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
                return render(request,'loguearse.html',{
                     'form': UserCreationForm,
                     'error': 'El usuario ya existe'
                })
        return render(request,'loguearse.html',{
            'form': UserCreationForm,
            'error': 'Contraseñas no coinciden'
    })

def oficina(request):
     return render(request, 'oficina.html')

def cerrarSesion(request):
     logout(request)
     return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html',{
                'form': AuthenticationForm,
                'error': 'Usuario o Contraseña incorrecto'
            })
        else:
            login(request, user)
            return redirect('oficina')
             