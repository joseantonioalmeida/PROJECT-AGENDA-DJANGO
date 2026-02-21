from typing import Any
from django.core.exceptions import ValidationError
from django import forms
from contact import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



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
                'placeholder':'Digite seu usuário'
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