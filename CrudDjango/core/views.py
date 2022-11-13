from distutils import core
from pyexpat import model
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm

# Create your views here.
def pagg2(request):
    return render(request, 'core\pagg2.html')

def pagg(request):
    libros = Libro.objects.all()
    return render(request, 'core\pagg.html', {'libros': libros})

def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('index')
    return render(request, 'core\libros\crear.html', {'formulario': formulario})

def editar(request, id):
    libros = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libros)
    return render(request, 'core\libros\editar.html', {'formulario': formulario})

def form(request):
    return render(request, 'core\libros\eformulario.html')

def libros(request):
    libros = Libro.objects.all()
    return render(request, 'core\libros\index.html', {'libros': libros})

def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('index')