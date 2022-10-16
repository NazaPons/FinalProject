from django import forms
from .models import Articulo
from django.contrib.auth.forms import UserCreationForm
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