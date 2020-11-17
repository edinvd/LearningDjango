from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import login
from django.contrib.auth import authenticate

def index(request):
    return render(request,'index.html', {
        'message' :  'Listado de productos',
        'title' : 'Productos',
        'products' : [
            {'title' : 'Playera', 'price' : 15, 'stock' : True},
            {'title' : 'Camisa', 'price' : 17, 'stock' : True},
            {'title' : 'Playera', 'price' : 25, 'stock' : True},
            {'title' : 'Casaca', 'price' : 15, 'stock' : False},
            {'title' : 'Blusa', 'price' : 12, 'stock' : True},
            {'title' : 'Zapatillas', 'price' : 20, 'stock' : False},
        ]
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username') #Diccionario
        password = request.POST.get('password') #None

        user = authenticate(username=username, password=password) #None
        if user:
            login(request, user)
            print("Usuario autenticado")
        else:
            print("Usuario no autenticado")
            
    return render(request, 'users/login.html', {

    })
