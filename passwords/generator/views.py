from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def password(request):
    caracteres= list('abcdeefghijklmnñopqrstuvxyz')
    longitud= int(request.POST['length'])
    password_generado=''
    for x in range(longitud):
        password_generado+=random.choice(caracteres)

    return render(request, 'password.html', {'password':password_generado})