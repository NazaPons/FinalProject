from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Articulo
from .forms import ArticuloForm, UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def articulos(request):
    articulos = Articulo.objects.all()
    return render(request, 'articulos/index.html', {'articulos': articulos})

def crear(request):
    formulario = ArticuloForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('articulos')
    return render(request, 'articulos/crear.html', {'formulario': formulario})

def editar(request, id):
    articulo= Articulo.objects.get(id=id)
    formulario = ArticuloForm(request.POST or None, request.FILES or None, instance=articulo)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('articulos')
    return render(request, 'articulos/editar.html', {'formulario': formulario})

def eliminar(request, id):
    articulo = Articulo.objects.get(id=id)
    articulo.delete()
    return redirect('articulos')

def perfil(request):
    return render(request, 'paginas/perfil.html')

def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado correctamente.')
            return redirect('inicio')
    else:
        form = UserRegisterForm()

    context = {'form': form} 
    return render(request, 'paginas/registro.html', context)