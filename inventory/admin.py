from django.contrib import admin

from .models import ItemLocation, Location, Item

admin.site.register(ItemLocation)
admin.site.register(Item)
admin.site.register(Location)