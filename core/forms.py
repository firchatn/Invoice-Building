from django import forms

class clientForm(forms.Form):
    nom = forms.CharField(max_length=100, widget=forms.TextInput(attrs={ 'placeholder': 'nom'}))
    prenom = forms.CharField(max_length=100, widget=forms.TextInput(attrs={ 'placeholder': 'prenom'}))
    telephone = forms.CharField(max_length=100, widget=forms.TextInput(attrs={ 'placeholder': 'telephone'}))
    adress = forms.CharField(max_length=100, widget=forms.TextInput(attrs={ 'placeholder': 'adress'}))
    codetva = forms.CharField(max_length=100, widget=forms.TextInput(attrs={ 'placeholder': 'code tva'}))

