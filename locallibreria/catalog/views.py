from django.shortcuts import render
from .models import Videojuego

# Create your views here.
def index(request):
	return render(request,
		'index.html',
		)

def ofertas(request):
	num_videojg = Videojuego.objects.all()
	return render(request,
		'ofertas.html',
		context={"num_videojg":num_videojg},
		)
def contacto(request):
	return render(request,
		'contacto.html',
		)
def iniciador(request):
	return render(request,
		'iniciador.html',
		)
def registrador(request):
	return render(request,
		'registrador.html',
		)