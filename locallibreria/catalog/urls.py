from django.urls import path 
from . import views
urlpatterns = [
	path('',views.index,name='index'),
	path('ofertas/',views.ofertas,name='ofertas'),
	path('contacto/',views.contacto,name='contacto'),
	path('registro',views.registrador,name='registrador'),
	path('inicioSesion',views.iniciador,name='iniciador')

]