from django import forms
from .models import Articulo
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = '__all__'

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1: forms.CharField(label= "Contraseña", widget= forms.PasswordInput)
    password2: forms.CharField(label= "Confirmar Contraseña", widget= forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserChangeForm):
    username = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Usuario: '}))
    email = forms.EmailField(widget= forms.TextInput(attrs={'placeholder': 'Email: '}))
    first_name = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Nombre: '}))
    last_name = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Apellido: '}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={'placeholder': 'Contraseña: '}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        help_texts = {k:"" for k in fields}

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label="", widget= forms.PasswordInput(attrs={'placeholder': "Vieja Contraseña: "}))
    new_password1 = forms.CharField(label="",widget= forms.PasswordInput(attrs={'placeholder': "Nueva Contraseña: "}))
    new_password2 = forms.CharField(label="",widget= forms.PasswordInput(attrs={'placeholder': "Confirmar nueva contraseña: "}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        help_texts = {k:"" for k in fields}