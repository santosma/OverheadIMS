from .models import ItemLocation
from .form import ItemLocationForm
from django.shortcuts import render, get_object_or_404


def item_detail_view(request):
	items_list = ItemLocation.objects.all()
	context = {
		'items' : items_list,
		'item' : None
	}
	return render(request,"inventory/item_base.html", context)


def item_create_view(request):
	form = ItemLocationForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ItemLocationForm()

	context = {
		'form' : form,
	}
	return render(request, "inventory/create.html", context)


def item_dynamic_view(request,id_lookup):
	item_single = get_object_or_404(ItemLocation, id=id_lookup)
	context = {
		'item': item_single,
		'items' : None
	}
	return render(request, "inventory/item_base.html", context)
	

