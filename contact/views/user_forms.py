from django.shortcuts import render, redirect
from contact.forms import RegisterForm
from django.contrib import messages

# Create your views here.

def register(request):
    form = RegisterForm()


    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'Usuário criado com sucesso!')
            return redirect('contact:index')
            
    return render(
        request, 
        'contact/register.html',
        {
            'form': form,
        }
        )