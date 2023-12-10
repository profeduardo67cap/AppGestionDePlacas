# from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

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
                    return HttpResponse('Usuario creado satisfactoriamente')
            except:
                 return HttpResponse('El usuario ya existe')
        return HttpResponse('No coinciden las contraseñas')




    return render(request,'logearse.html',{
        'form': UserCreationForm
    })