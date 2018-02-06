from django.shortcuts import render, redirect
from .forms import clientForm

# Create your views here.
def facture(request):
	return render(request,'core/facture.html')

def index(request):
	return render(request,'core/home.html')

def client(request):
	if request.method == "POST":
			form = clientForm(request.POST)
			if form.is_valid():
				vnom = form.cleaned_data['nom']
				vprenom = form.cleaned_data['prenom']
				vadress = form.cleaned_data['adress']
				vtel = form.cleaned_data['telephone']
				vcodetva = form.cleaned_data['codetva']
				print(vtel)
				return redirect('core:index')
	else:
		form = clientForm()

	return render(request,'core/client.html',
                      {'form' : form })