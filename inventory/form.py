from django import forms
 
from .models import ItemLocation

class ItemLocationForm(forms.ModelForm):
	class Meta:
		model = ItemLocation
		fields = [
			'sku',
			'loc',
			'qty'
		]
			
