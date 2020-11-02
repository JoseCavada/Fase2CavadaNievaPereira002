from django.test import TestCase
from catalog.models import Videojuego 
class PruebaM(TestCase):
	@classmethod

	def setUpTestData(cls):
		Videojuego.objects.create(id='21a49a5b-9d10-4964-bf2d-24c1b97fe351',nombre='nombre', genero='Juego de rol', precio=100000, ESRB='Todos', descripcion='descripcion')
	
	def test_nombre_label(self):
		videojuego=Videojuego.objects.get(id='21a49a5b-9d10-4964-bf2d-24c1b97fe351')
		field_label = Videojuego._meta.get_field('nombre').verbose_name
		self.assertEquals(field_label,'nombre')

	def test_genero_label(self):
		videojuego=Videojuego.objects.get(id='21a49a5b-9d10-4964-bf2d-24c1b97fe351')
		field_label = Videojuego._meta.get_field('genero').verbose_name
		self.assertEquals(field_label,'genero')

	def test_precio_label(self):
		videojuego=Videojuego.objects.get(id='21a49a5b-9d10-4964-bf2d-24c1b97fe351')
		field_label = Videojuego._meta.get_field('precio').verbose_name
		self.assertEquals(field_label,'precio')

	def test_ESRB_label(self):
		videojuego=Videojuego.objects.get(id='21a49a5b-9d10-4964-bf2d-24c1b97fe351')
		field_label = Videojuego._meta.get_field('ESRB').verbose_name
		self.assertEquals(field_label,'ESRB')

	def test_descripcion_label(self):
		videojuego=Videojuego.objects.get(id='21a49a5b-9d10-4964-bf2d-24c1b97fe351')
		field_label = Videojuego._meta.get_field('descripcion').verbose_name
		self.assertEquals(field_label,'descripcion')