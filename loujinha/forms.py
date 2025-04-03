# meu_app/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models.product import Product
from .models.custom_user import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'cpf', 'address']

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if not self.instance._cpf_validation(cpf):
            raise forms.ValidationError("CPF inválido.")
        return cpf

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Usuário", widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={"class": "form-control"}))

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price', 'description', 'quantity','cover', 'category']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
    
    
