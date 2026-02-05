from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produktow, name='lista_produktow'),
    path('produkt/<int:pk>/', views.szczegoly_produktu, name='szczegoly_produktu'),
    path('produkt/<int:pk>/awaria/', views.zglos_awarie, name='zglos_awarie'),
    path('awarie/', views.lista_awarii, name='lista_awarii'),
    path('dostepne/', views.tylko_dostepne, name='tylko_dostepne'),
]