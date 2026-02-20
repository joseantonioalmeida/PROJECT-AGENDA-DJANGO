from django.shortcuts import redirect, render
from contact.forms import ContactForms

# Create your views here.

def create(request):
    if request.method == 'POST':
        form = ContactForms(request.POST)
        context = {
            'form': form,
        }    

        # se o form não estiver nenhum erro, ou seja for válido.
        if form.is_valid():
            form.save()
            return redirect('contact:create')

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