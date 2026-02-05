from django.shortcuts import render, get_object_or_404, redirect
from .models import Produkt
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