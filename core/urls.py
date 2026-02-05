from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produktow, name='lista_produktow'),
]