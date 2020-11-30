from django import forms
from .models import Hospital


class Hospitalform(forms.ModelForm):
	class Meta:
		"""docstring for meta"""
		model = Hospital
		fields = '__all__'
