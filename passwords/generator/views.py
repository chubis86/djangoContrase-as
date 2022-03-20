from webbrowser import get
from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def password(request):
    caracteres= list('abcdefghijklmnñopqrstuvxyz')
    
    if 'especiales' in request.POST:
        caracteres.extend(list('!"#$%&/()'))

    if 'uppercase' in request.POST:
        caracteres.extend(list('ABCDEFGHIJKLMNÑOPQRSTUVXYZ'))

    if 'numeros' in request.POST:
        caracteres.extend(list('0123456789'))
        
    longitud= int(request.POST['length'])
    password_generado=''
    
    for x in range(longitud):
        password_generado+=random.choice(caracteres)
    
    return render(request, 'password.html', {'password':password_generado})