from django.shortcuts import render, get_object_or_404, redirect
from contact import models
from django.db.models import Q
from django.db.models import Value
from django.db.models.functions import Concat

# Create your views here.

def index(request):
    contacts = models.Contact.objects\
        .filter(show=True)\
        .order_by('-id')[10:30]
    
    # QuerySets
    # print(contacts.query)

    context = {
        'contacts': contacts,
        'site_title': 'Contatos - '
    }    
    return render(
        request,
        'contact/index.html',
        context= context,
    )


def search(request):
    search_value = request.GET.get('q', '').strip() 

    if search_value == '':
        return redirect('contact:index')
    
    contacts = models.Contact.objects\
        .annotate(
            full_name_db=Concat('first_name', Value(' '), 'last_name')
        )\
        .filter(show=True)\
        .filter(
            Q(full_name_db__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__icontains=search_value)
                )\
        .order_by('-id')
    
    # QuerySets
    # print(contacts.query)

    context = {
        'contacts': contacts,
        'site_title': 'Search - ',
        'search_value': search_value,
    }    
    return render(
        request,
        'contact/index.html',
        context= context,
    )

def contact(request, contact_id):
    # single_contact = models.Contact.objects.filter(pk=contact_id).first()

    # if single_contact is None:
    #     raise Http404()
    
    single_contact = get_object_or_404(
        models.Contact.objects.filter(pk=contact_id, show=True),
        )

    site_title = f'{single_contact.first_name} {single_contact.last_name} - '
    context = {
        'contact': single_contact,
        'site_title': site_title,
    }    
    return render(
        request,
        'contact/contact.html',
        context= context,
    )