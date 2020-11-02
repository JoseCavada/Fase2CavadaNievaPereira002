from django.urls import path 
from . import views
urlpatterns = [
	path('',views.index,name='index'),
	path('ofertas/',views.ofertas,name='ofertas'),
	path('contacto/',views.contacto,name='contacto'),
	path('registro',views.registrador,name='registrador'),
	path('inicioSesion',views.iniciador,name='iniciador'),
	path('videojuego/<pk>',views.VideojuegoDetailView.as_view(),name='videojuego_detail'),

]
urlpatterns += [
	path('videojuego/create/',views.VideojuegoCreate.as_view(),name='videojuego_create'),
	path('videojuego/<pk>/update/',views.VideojuegoUpdate.as_view(),name='videojuego_update'),	
	path('videojuego/<pk>/delete/',views.VideojuegoDelete.as_view(),name='videojuego_delete'),

]