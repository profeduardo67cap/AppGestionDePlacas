from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import OficinaForm
from .models import Oficina


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
     oficinas = Oficina.objects.all
     return render(request, 'oficina.html', {
         'oficinas': oficinas
     })

def oficinaCrear(request):
    if request.method == 'GET':
        return render(request, 'oficinaCrear.html',{
            'form': OficinaForm
        })
    else:
        try:
            form = OficinaForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('oficina')
        except ValueError:
            return render(request, 'oficinaCrear.html',{
            'form': OficinaForm,
            'error': 'Por favor provee datos válidos'
        })

def oficinaDetalle(request, oficinaId):
    # oficina = Oficina.objects.get(pk=oficinaId)
    oficina = get_object_or_404(Oficina,pk=oficinaId)
    return render(request, 'oficinaDetalle.html', {'oficina': oficina })

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
             