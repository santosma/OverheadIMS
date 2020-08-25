from django.shortcuts import render, get_object_or_404
from .models import ItemLocation
from .form import ItemLocationForm

def item_detail_view(request):
	objs = ItemLocation.objects.all()
	context ={
		'items_list' : objs
	}
	return render(request,"item/details.html",context)


def item_create_view(request):
	form = ItemLocationForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ItemLocationForm()

	context = {
		'form' : form
	}
	return render(request, "item/create.html", context)


def item_dynamic_view(request,id_lookup):
	obj = get_object_or_404(Inventory, id=id_lookup)
	context = {
		"object" : obj
	}
	return render(request, "item/details.html", context)
	

