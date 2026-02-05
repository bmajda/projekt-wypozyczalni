from django.shortcuts import render
from .models import Produkt

def lista_produktow(request):
    # Pobieramy wszystkie produkty z bazy danych
    produkty = Produkt.objects.all()
    
    # Przekazujemy je do szablonu HTML
    return render(request, 'core/lista_produktow.html', {'produkty': produkty})