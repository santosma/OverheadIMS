from django.db import models

class account(models.Model):
	"""Users"""
	name = models.CharField(max_length=25, null=True)
	date_created = models.DateTimeField(auto_now_add=True)
		
