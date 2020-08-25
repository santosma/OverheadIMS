from django.db import models

# Create your models here.

class ItemLocation(models.Model):
	loc = models.CharField(max_length=5)
	sku = models.CharField(max_length=10)
	qty = models.PositiveSmallIntegerField(default=0)

	def __str__(self):
		return self.loc + self.sku + str(self.qty)

