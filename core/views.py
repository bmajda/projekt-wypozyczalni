from django.shortcuts import render, get_object_or_404, redirect
from .models import Produkt, Awaria
from .forms import AwariaForm

def lista_produktow(request):
    produkty = Produkt.objects.all()
    return render(request, 'core/lista_produktow.html', {'produkty': produkty})

def szczegoly_produktu(request, pk):
    produkt = get_object_or_404(Produkt, pk=pk)
    return render(request, 'core/szczegoly_produktu.html', {'produkt': produkt})

def zglos_awarie(request, pk):
    produkt = get_object_or_404(Produkt, pk=pk)
    
    if request.method == "POST":
        form = AwariaForm(request.POST)
        if form.is_valid():
            awaria = form.save(commit=False)
            awaria.produkt = produkt
            awaria.save()
            produkt.dostepny = False
            produkt.save()
            
            return redirect('szczegoly_produktu', pk=pk)
    else:
        form = AwariaForm()

    return render(request, 'core/zglos_awarie.html', {'form': form, 'produkt': produkt})

def lista_awarii(request):
    awarie = Awaria.objects.all().order_by('-data_zgloszenia')
    return render(request, 'core/lista_awarii.html', {'awarie': awarie})

def tylko_dostepne(request):
    produkty = Produkt.objects.filter(dostepny=True)
    return render(request, 'core/tylko_dostepne.html', {'produkty': produkty})