from django.urls import path

from . import views

urlpatterns = [
   	path('inventory/', views.item_detail_view),
    path('create/', views.item_create_view),
]	