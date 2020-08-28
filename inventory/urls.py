from django.urls import path

from . import views

urlpatterns = [
   	path('inventory/', views.item_detail_view),
    path('create/', views.item_create_view),
    path('inventory/<int:id_lookup>/', views.item_dynamic_view)
]	