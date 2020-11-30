from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    #return HttpResponse("<h1>Aqui é index<h1>")
    return render(request, 'hospitais/index.html')

def hospitais(request):
    return HttpResponse("<h1>Aqui é area Hospital<h1>")