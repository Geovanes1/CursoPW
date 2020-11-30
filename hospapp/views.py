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
    if request.method == "POST":
    	form = Hospitalform(request.POST, request.FILES)
    	if form.is_valid():
    		hosp = form.save()
    		hosp.save()
    		form=Hospitalform()
    return render(request, 'hospitais/criar_hospitais.html',{'form':form})