from django.shortcuts import render
from django.http import HttpResponse

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

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username') #Diccionario
        password = request.POST.get('password') #None

        print(username)
        print(password)

    return render(request, 'users/login.html', {

    })