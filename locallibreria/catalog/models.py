from django.db import models    #Definir modelos
from django.urls import reverse #direccionar los modelos a urls
import uuid						#permite reconocer los campos clave de una clase

# Create your models here.
class Videojuego(models.Model):
 	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text= 'Id única de este videojuego para toda la tienda')
 	nombre = models.CharField(max_length=200)

 	ENUM_GENERO = (
 		('RPG', 'Juego de rol'),
 		('Acc','Accion'),
 		('Ave','Aventuras'),
 		('Sbx','Mundo abierto'),
 		('Plt','Plataformas'),
 		('VR', 'Realidad virtual'),
 		('Ter','Terror'),
 		('BR','Battle royale'),
 		('Otr','Otro genero'),
 		)
 	genero = models.CharField(
 		max_length = 3,
 		choices=ENUM_GENERO,
 		blank=True,
 		default='Otr',
 		help_text = 'Generos de videojuegos'
 		)

 	precio = models.IntegerField()

 	ENUM_ESRB = (
 		('E','Todos'),
 		('E+10','Todos los mayores a 10'),
 		('T','Adolescentes'),
 		('M','Mayores a 17'),
 		('A','Solo adultos'),
 		('RP','Clasificación pendiente'),
 		)

 	ESRB = models.CharField(
 		max_length = 4,
 		choices = ENUM_ESRB,
 		blank = True,
 		default = 'RP',
 		help_text = 'Clasificacion de edad recomendada para jugar',
 		)

 	def __str__(self):
 		"""String que representa el modelo del objeto"""
 		return f'(self.id) ((self.nombre))'