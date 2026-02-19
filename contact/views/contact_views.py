from django.shortcuts import render
from contact import models

# Create your views here.

def index(request):
    contacts = models.Contact.objects\
        .filter(show=True)\
        .order_by('-id')[10:30]
    
    # QuerySets
    # print(contacts.query)

    context = {
        'contacts': contacts,
    }    
    return render(
        request,
        'contact/index.html',
        context= context,
    )