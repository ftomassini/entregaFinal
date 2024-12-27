from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label="Nombre")
    last_name = forms.CharField(max_length=30, required=True, label="Apellido")
    email = forms.EmailField(required=True, label="Email")
    bio = forms.CharField(widget=forms.Textarea, required=False, label="Biografía")
    avatar = forms.ImageField(required=False, label="Avatar")

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'bio', 'avatar','password1', 'password2']
