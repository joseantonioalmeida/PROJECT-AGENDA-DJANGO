from typing import Any
from django.core.exceptions import ValidationError
from django import forms
from contact import models


class ContactForms(forms.ModelForm):
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