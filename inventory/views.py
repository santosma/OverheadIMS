from .models import ItemLocation
from .form import ItemLocationForm
from django.shortcuts import render, get_object_or_404


def item_detail_view(request):
	items_list = ItemLocation.objects.all()
	single_flag = False
	context = {
		'items' : items_list,
		'single': single_flag
	}
	return render(request,"item/item_base.html", context)


def item_create_view(request):
	form = ItemLocationForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ItemLocationForm()

	context = {
		'form' : form,
	}
	return render(request, "item/create.html", context)


def item_dynamic_view(request,id_lookup):
	item_single = get_object_or_404(ItemLocation, id=id_lookup)
	single_flag = True
	context = {
		'items': item_single,
		'single': single_flag
	}
	return render(request, "item/item_base.html", context)
	

