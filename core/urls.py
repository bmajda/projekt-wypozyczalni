from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produktow, name='lista_produktow'),
    path('produkt/<int:pk>/', views.szczegoly_produktu, name='szczegoly_produktu'),
]