from django.shortcuts import render, get_object_or_404
from .models import Produkt

def lista_produktow(request):
    produkty = Produkt.objects.all()
    return render(request, 'core/lista_produktow.html', {'produkty': produkty})

def szczegoly_produktu(request, pk):
    produkt = get_object_or_404(Produkt, pk=pk)
    return render(request, 'core/szczegoly_produktu.html', {'produkt': produkt})