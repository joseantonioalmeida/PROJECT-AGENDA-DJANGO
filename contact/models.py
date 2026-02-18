from django.db import models
from django.utils import timezone

# Create your models here.
# qualquer coisa que a gnt fazer no model temos que executar esse 
# seguinte comando: python manage.py makemigrations, python manage.py migrate



# id (Primary key)
# first_name(string), last_name(string), phone(String)
# email(email), created_date(date), description(text)

# Depois
# category(foreign key), show(boolean), owner(foreign key)
# picture (imagem)

# a gnt vai usar o contact pra create, select(buscar), update e delete(CRUD)
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    create_date = models.DateTimeField(default=timezone.now)
    description =models.TextField(blank=True) #blank -> Opcional
