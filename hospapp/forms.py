from django import forms
from .models import Hospital


class Hospitalform(forms.ModelForm):
	class Meta:
		"""docstring for meta"""
		model = Hospital
		fields = '__all__'
		# fields = ['nome_hospital','foto','desc_hospital','tipo_hospital','conceito_hospital']
