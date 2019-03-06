from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(error_messages={'required': 'Это поле обязательно.'})
    first_name = forms.CharField(max_length=50, required=True, error_messages={'max_length': 'Максимальная длина возможного имени - 50.', 'required': 'Это поле обязательно.'})
    email = forms.EmailField(max_length=254, required=True, error_messages={'max_length': 'Максимальная длина почты - 254.', 'required': 'Это поле обязательно.'})

    error_messages = {
        'required': 'Это поле обязательно.',
        'password_mismatch': "Пароли не совпадают!",
    }

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password1', 'password2')