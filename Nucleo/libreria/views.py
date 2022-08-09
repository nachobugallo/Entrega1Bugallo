from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from libreria.models import Books
from libreria.forms import Formulario_Books


def saludo(request):
    greeting= "Bienvenido"
    context = {'greeting':greeting}
    return render (request, "home.html", context=context)


def create_product(request):
    
    if request.method == 'POST':
        form = Formulario_Books(request.POST)

        if form.is_valid():
            Books.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                author = form.cleaned_data['author'],
                is_active = form.cleaned_data['is_active'],
                book_is_atp = form.cleaned_data['book_is_atp'],
                book_category = form.cleaned_data['book_category'],
                stock = form.cleaned_data['stock']
            )
            return redirect(create_product)

    elif request.method == 'GET':
        form = Formulario_Books()
        context = {'form':form}
        return render(request, 'productos/new-prod.html', context=context)

def list_prod(request):
    books = Books.objects.all()
    context = {
        'books': books
    }
    return render(request, 'productos/list-prod.html', context=context)

def search_prod(request):
    search = request.GET['search']
    products = Books.objects.get(name__icontains=search) 
    context = {'products':products}
    return render(request, 'productos/search-prod.html', context=context)