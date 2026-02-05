from django.contrib import admin
from .models import Kategoria, Producent, Produkt, Wypozyczenie, Awaria

admin.site.register(Kategoria)
admin.site.register(Producent)
admin.site.register(Produkt)
admin.site.register(Wypozyczenie)
admin.site.register(Awaria)