from django.db import models
from django.contrib.auth.models import User  # Importujemy wbudowanego użytkownika

# Model 1: Kategoria sprzętu
class Kategoria(models.Model):
    nazwa = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name_plural = "Kategorie"

# Model 2: Producent sprzętu
class Producent(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.TextField(blank=True)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name_plural = "Producenci"

# Model 3: Konkretny produkt (sprzęt)
class Produkt(models.Model):
    nazwa = models.CharField(max_length=200)
    opis = models.TextField(blank=True)
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE)
    producent = models.ForeignKey(Producent, on_delete=models.SET_NULL, null=True, blank=True)
    dostepny = models.BooleanField(default=True)  # Czy sprzęt jest teraz wolny?
    
    def __str__(self):
        return f"{self.nazwa} ({self.producent})"

    class Meta:
        verbose_name_plural = "Produkty"

# Model 4: Historia wypożyczeń
class Wypozyczenie(models.Model):
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE) # Kto wypożycza
    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE) # Co wypożycza
    data_wypozyczenia = models.DateField(auto_now_add=True)
    data_zwrotu = models.DateField(null=True, blank=True) # Puste jeśli jeszcze nie oddał
    
    def __str__(self):
        return f"{self.uzytkownik} - {self.produkt}"

    class Meta:
        verbose_name_plural = "Wypożyczenia"

# Model 5: Zgłoszenie awarii (spełnia wymóg o zniszczonym sprzęcie)
class Awaria(models.Model):
    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE)
    opis_usterki = models.TextField()
    data_zgloszenia = models.DateTimeField(auto_now_add=True)
    czy_naprawione = models.BooleanField(default=False)

    def __str__(self):
        return f"Awaria: {self.produkt.nazwa}"

    class Meta:
        verbose_name_plural = "Awarie"