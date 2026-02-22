from typing import Any
from django.core.exceptions import ValidationError
from django import forms
from contact import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation



class ContactForms(forms.ModelForm):



    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'placeholder':'Aqui veio da classe ContactForms'
    #         }
    #     ),
    #     label= 'Primeiro Nome',
    #     help_text='Digite seu primeiro nome'
    # )

    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*'
            }
        )
    )

    class Meta:
        model = models.Contact  
        fields = (
            'first_name', 'last_name', 'phone', 'email','description', 
            'category', 'picture',
            )
        
    def clean(self) -> dict[str, Any]:
        # o método clean tem acesso a todos os campos do meu form

        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        if first_name==last_name:
            msg = ValidationError(    
                        'Primeiro nome não pode ser igual ao segundo',
                        code='invalid'
                )
            self.add_error('first_name',msg)
            self.add_error('last_name',msg)
       
        return super().clean()
    
    def clean_first_name(self) -> str:
        first_name = self.cleaned_data.get('first_name')
        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(    
                        'Nome inválido',
                        code='invalid'
                )
            )

        return first_name #type:ignore 
    
class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # isso remove o autofocus do field username que o django colocou
        self.fields['username'].widget.attrs.pop('autofocus', None)

    first_name = forms.CharField(
        required=True,
        min_length=3,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Digite seu primeiro nome'
                }
        )
    )
    last_name = forms.CharField(
        required=True,
        min_length=3,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Digite seu último nome'
                }
        )
    )
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Digite seu e-mail'
                }
        )
    )
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Digite seu usuário',
                }
        )
    )
    class Meta:
        model = User

        fields = (
            'first_name', 'last_name', 'email', 'username',
            'password1', 'password2',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError(
                    'Já existe este e-mail cadastrado.',
                    code='invalid',
                )
            )

        return email

class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        label='Primeiro Nome',
        required=True,
        min_length=3,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Digite seu primeiro nome'
                }
        )
    )

    last_name = forms.CharField(
        label='Último Nome',
        required=True,
        min_length=3,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Digite seu último nome'
                }
        )
    )
    email = forms.EmailField(
        required=True,
    )
    password1 = forms.CharField(
        label='Senha',
        strip=False,
        required=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label='Confirmar Senha',
        strip=False,
        required=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),

    )
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'username',
        )

    def clean(self) -> dict[str, Any]:
        password1 = self.cleaned_data.get('password1')  
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('As Senhas não são iguais.')
                )

        return super().clean()


    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if current_email !=email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError(
                        'Já existe este e-mail cadastrado.',
                        code='invalid',
                    )
            )

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        
        password = cleaned_data.get('password1')
        if password:
            user.set_password(password)
        if commit:
            user.save()

        return user
                


    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if not password1:
            try:
                password_validation.validate_password(password1) #type:ignore
            except ValidationError as errors:
                self.add_error(
                    'password1',
                    ValidationError(errors),
                    )

        return password1