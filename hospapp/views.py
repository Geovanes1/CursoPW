from django.shortcuts import render
from django.http import HttpResponse
from .forms import Hospitalform
# Create your views here.

def index(request):
    #return HttpResponse("<h1>Aqui é index<h1>")
    return render(request, 'hospitais/index.html')

def hospitais(request):
    #return HttpResponse("<h1>Aqui é area Hospital<h1>")
    return render(request, "hospitais/hospitais.html")

def criar_hospital(request):
    form = Hospitalform(request.POST)
    return render(request, 'hospitais/criar_hospitais.html',{'form':form})