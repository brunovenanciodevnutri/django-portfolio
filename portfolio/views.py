from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    """Página principal do Portfólio"""
    return render(request, 'index.html', {'título': 'Bem-vindo ao meu Portfólio'})

def ola(request):
    """Página principal do Portfólio"""
    return HttpResponse('Olá Django')