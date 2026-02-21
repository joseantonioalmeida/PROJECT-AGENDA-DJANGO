from django.shortcuts import render, get_object_or_404, redirect
from contact import models
from django.core.paginator import Paginator
from contact.forms import RegisterForm

# Create your views here.

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            
    return render(
        request, 
        'contact/register.html',
        {
            'form': form,
        }
        )