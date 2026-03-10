from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #O Django buscará automaticamente dentro da pasta templates
    return render(request, 'associado/index.html')
    return HttpResponse('<h1>SindApp</h1><p>Bem-vindo ao portal do associado!</p>')
