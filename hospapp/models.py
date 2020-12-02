from django.db import models
from PIL import Image

# Create your models here.
class Hospital (models.Model):

	nome_hospital = models.CharField(max_length=200)
	foto = models.ImageField(null=True, blank=200)
	desc_hospital = models.CharField(max_length=200)
	tipo_hospital = models.CharField(max_length=200)
	conceito_hospital = models.CharField(max_length=200)


	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		im = Image.open(self.foto.path)
		novo_tamanho = (250,250)
		im.thumbnail(novo_tamanho)
		im.save(self.foto.path)


	def foto_url(self):
		if self.foto and hasattr(self.foto, 'url'):
			print("A url da foto é:", self.foto.url)
			return self.foto.url
		else:
			return "/static/img/paisagem02.jpg"


	def __str__(self):
		return self.nome_hospital