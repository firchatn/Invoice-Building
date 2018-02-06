from django.shortcuts import render

# Create your views here.
def facture(request):
	return render(request,'core/facture.html')

def index(request):
	return render(request,'core/home.html')
