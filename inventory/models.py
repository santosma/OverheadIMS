from django.db import models

# Create your models here.


class Location(models.Model):
	loc = models.CharField(max_length=5)
	def __str__(self):
		return self.loc 	

class Item(models.Model):
	sku = models.CharField(max_length=10) 
	def __str__(self):
		return self.sku 

class ItemLocation(models.Model):
	loc = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)
	sku = models.ForeignKey(Item, null=True, on_delete=models.SET_NULL)
	qty = models.PositiveSmallIntegerField(default=0)

	def __str__(self):
		return self.loc + self.sku + str(self.qty)

