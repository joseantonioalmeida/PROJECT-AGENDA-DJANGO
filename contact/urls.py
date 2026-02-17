from django.urls import path
from contact import views

app_name = 'contact'

# contact/
urlpatterns = [
    path('', views.index, name='index'),
]
