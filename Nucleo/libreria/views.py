from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from libreria.models import Books, Bindings, Personalnotebook
from libreria.forms import Formulario_Books, Formulario_Bindings, Formulario_Personalnotebook


def home(request):
    return render(request, "home.html", context={})
def saludo(request):
    greeting= "Bienvenido"
    context = {'greeting':greeting}
    return render (request, "home.html", context=context)

def quienes_somos(request):

    return render (request, "quienes_somos.html", context={})

def contacto(request):

    return render (request, "contacto.html", context={})
    


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
    return render(request, 'productos/lista-prod.html', context=context)

def search_prod(request):
    search = request.GET['search']
    books = Books.objects.filter(name__icontains=search) 
    context = {'books':books}
    return render(request, 'productos/search-prod.html', context=context)


def delete_product(request, pk):
    if request.method == 'GET':
        book = Books.objects.get(pk = pk)
        context = {'book': book}
        return render(request, 'productos/delete_product.html', context= context)
    elif request.method == 'POST':
        book = Books.objects.get(pk = pk)
        book.delete()
        return redirect(list_prod)

def update_product(request, pk):
    if request.method == 'POST':
        form = Formulario_Books(request.POST)
        if form.is_valid():
            book =Books.objects.get(id=pk)
            book.name = form.cleaned_data['name']
            book.price = form.cleaned_data['price']
            book.author = form.cleaned_data['author']
            book.is_active = form.cleaned_data['is_active']
            book.book_is_atp = form.cleaned_data['book_is_atp']
            book.book_category = form.cleaned_data['book_category']
            book.stock = form.cleaned_data['stock']
            book.save()
            return redirect(list_prod)
                

    elif request.method == 'GET':
        book = Books.objects.get(id=pk)


        form = Formulario_Books(initial={'name':book.name, 
                                        'price':book.price, 
                                        'author':book.author,
                                        'is_active':book.is_active,
                                        'book_is_atp':book.book_is_atp,
                                        'book_category':book.book_category,
                                        'stock':book.stock})
        context = {'form': form}
        return render(request, 'productos/update_product.html', context = context)





def list_bind(request):
    bindings = Bindings.objects.all()
    context = {
        'bindings': bindings
    }
    return render(request, 'productos/list-bind.html', context)

def search_bind(request):
    search = request.GET['search']
    products = Bindings.objects.get(name__icontains=search) 
    context = {'products':products}
    return render(request, 'productos/  ', context=context)

def list_notebook(request):
    notebooks = Personalnotebook.objects.all()
    context = {
        'notebooks': notebooks
    }
    return render(request, 'productos/list-notebook.html', context=context)

def search_notebooks(request):
    search = request.GET['search']
    products = Personalnotebook.objects.get(name__icontains=search) 
    context = {'products':products}
    return render(request, 'productos/   ', context=context)

def create_binding(request):

    if request.method == 'POST':
        form = Formulario_Bindings(request.POST)

        if form.is_valid():
            Bindings.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                bind_size = form.cleaned_data['bind_size'],
                book_is_hardcover = form.cleaned_data['book_is_hardcover'],
                colorbook = form.cleaned_data['colorbook']
            )
            return redirect(create_binding)
    
    elif request.method == 'GET':
        form = Formulario_Bindings()
        context = {'form':form}
        return render(request, 'productos/new-binding.html', context=context)

def create_notebook(request):

    if request.method == 'POST':
        form = Formulario_Personalnotebook(request.POST)

        if form.is_valid():
            Personalnotebook.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                bind_size = form.cleaned_data['bind_size'],
                book_is_hardcover = form.cleaned_data['book_is_hardcover'],
                colorbook = form.cleaned_data['colorbook']
            )
            return redirect(create_notebook)
    
    elif request.method == 'GET':
        form = Formulario_Personalnotebook()
        context = {'form':form}
        return render(request, 'productos/new-notebook.html', context=context)