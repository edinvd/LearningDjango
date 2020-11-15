from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html', {
        'message' :  "Hello world!. I'm Edin",
        'title' : "Título",
    })
