from django.contrib import admin

# Register your models here.
from .models import Client, Facture

admin.site.register(Facture)
admin.site.register(Client)