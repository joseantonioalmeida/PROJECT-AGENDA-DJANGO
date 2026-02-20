from typing import Any

from django.shortcuts import render, get_object_or_404, redirect
from contact import models
from django.db.models import Q
from django.core.paginator import Paginator
from django.core.exceptions import ValidationError
from django import forms

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

# Create your views here.

def create(request):
    if request.method == 'POST':
        context = {
            'form': ContactForms(data=request.POST),
        }    
        return render(
            request,
            'contact/create.html',
            context= context,
        )
    

    context = {
        'form': ContactForms(),
    }    
    return render(
        request,
        'contact/create.html',
        context= context,
    )