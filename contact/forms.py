from typing import Any, Mapping
from django.core.exceptions import ValidationError
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from contact import models


class ContactForms(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder':'Aqui veio da classe ContactForms'
            }
        ),
        label= 'Primeiro Nomes',
        help_text='Digite seu primeiro nome'
    )
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    class Meta:
        model = models.Contact  
        fields = (
            'first_name', 'last_name',
            )
        
    def clean(self) -> dict[str, Any]:

        self.add_error(
            'first_name',
            ValidationError(    
                    'Mensagem de erro',
                    code='invalid'
            )
        )
        self.add_error(
            None,
            ValidationError(    
                    'Mensagem de erro 2',
                    code='invalid'
            )
        )
        return super().clean()