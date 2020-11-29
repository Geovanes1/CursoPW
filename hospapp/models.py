from django.db import models
from PIL import Image

# Create your models here.
class Hospital (models.Model):

	nome_hospital = models.CharField(max_length=200)
	foto = models.ImageField(null=True, blank=200)
	desc_hospital = models.CharField(max_length=200)
	tipo_hospital = models.CharField(max_length=200)
	conceito_hospital = models.CharField(max_length=200)

	def __str__(self):
		return self.nome_hospital