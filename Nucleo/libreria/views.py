from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

def saludo(request):
    greeting= "Bienvenido"
    context = {'greeting':greeting}
    return render (request, "home.html", context=context)
