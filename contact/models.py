from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# qualquer coisa que a gnt fazer no model temos que executar esse 
# seguinte comando: python manage.py makemigrations, python manage.py migrate



# id (Primary key)
# first_name(string), last_name(string), phone(String)
# email(email), created_date(date), description(text)
# category(foreign key), show(boolean), picture (image)
# owner(foreign key)


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
    #self.pk -> é da super
        return self.name


# a gnt vai usar o contact pra create, select(buscar), update e delete(CRUD)
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    create_date = models.DateTimeField(default=timezone.now)
    description =models.TextField(blank=True) #blank -> Opcional
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, 
        null=True, blank=True
            )
    owner = models.ForeignKey(
    User,
    on_delete=models.SET_NULL,
    blank=True, null=True
)
    
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'.strip()

    def __str__(self) -> str:
        #self.pk -> é da super
        return f'{self.first_name} {self.last_name}' 

