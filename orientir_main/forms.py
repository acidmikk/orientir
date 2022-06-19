from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class ContactForm(forms.Form):
    email = forms.EmailField(label='Email', required=True)
    name = forms.CharField(label='Имя', required=True)
    mess = forms.CharField(label='Сообщение', widget=forms.Textarea, required=True)


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control  required'}))
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control  required'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control  required'}))
    password2 = forms.CharField(label='Повтор пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-control  required'}))

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control required'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control required'}))
