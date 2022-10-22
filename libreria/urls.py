from unicodedata import name
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('articulos', views.articulos, name='articulos'),
    path('articulos/crear', views.crear, name='crear'),
    path('articulos/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('articulos/editar/<int:id>', views.editar, name='editar'),

    path('registro/', views.registro, name='registro'),
    path('login/', LoginView.as_view(template_name='paginas/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='paginas/logout.html'), name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('editarPerfil/', views.editarPerfil, name='editarPerfil'), 
    path('cambiarContraseña/', views.cambiarContraseña, name='cambiarContraseña'),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)