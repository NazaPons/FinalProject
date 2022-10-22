from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Articulo
from .forms import ArticuloForm, UserRegisterForm, UserEditForm, ChangePasswordForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
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

def editarPerfil(request):
    usuario = request.user
    user_basic_info = User.objects.get(id = usuario.id)
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance = usuario)
        if form.is_valid():
            #Datos que se van a actualizar
            user_basic_info.username = form.cleaned_data.get('username')
            user_basic_info.email = form.cleaned_data.get('email')
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')
            user_basic_info.save()
            return render(request, 'paginas/perfil.html')
    else:
        form = UserEditForm(initial={'email': usuario.email, 'username': usuario.username, 'first_name': usuario.first_name, 'last_name': usuario.last_name })
    return render(request, 'paginas/editarPerfil.html', {'form': form, 'usuario': usuario})

def cambiarContraseña(request):
    usuario = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(data = request.POST, user = request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return render(request, 'perfil.html')
    else:
        form = ChangePasswordForm(user = request.user)
    return render(request, 'changepass.html', {'form': form, 'usuario': usuario})