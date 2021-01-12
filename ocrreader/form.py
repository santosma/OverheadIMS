from django import forms

class UploadOcrFile(forms.Form):
	file = forms.ImageField()