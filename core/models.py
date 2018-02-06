from __future__ import unicode_literals

from django.db import models

class Client(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    tel = models.CharField(max_length=20)
    adress = models.CharField(max_length=20)
    codetva = models.CharField(max_length=200)
    add_date = models.DateTimeField(
        'date published', auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.nom

class Facture(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    somme = models.CharField(max_length=20)
    produitun = models.CharField(max_length=200)
    produitdeux = models.CharField(max_length=200, blank=True)
    produittrois = models.CharField(max_length=200, blank=True)
    produitquatre = models.CharField(max_length=200, blank=True)
    produitcinq = models.CharField(max_length=200, blank=True)
    produitsix = models.CharField(max_length=200, blank=True)
    produitsept = models.CharField(max_length=200, blank=True)
    create_date = models.DateTimeField(
        'date published', auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.somme
