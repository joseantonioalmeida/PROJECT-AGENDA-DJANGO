from django.urls import path
from contact import views

app_name = 'contact'

# 127.0.0.1/
urlpatterns = [
    path('<int:contact_id>/', views.contact, name='contact'),
    path('', views.index, name='index'),
]
