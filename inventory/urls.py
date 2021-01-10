from django.urls import path
from django.contrib import admin
from . import views

app_name='inventory'

urlpatterns = [
    path('', views.item_detail_view, name='all-items'),
    path('create/', views.item_create_view, name='create'),
    path('<int:id_lookup>/', views.item_dynamic_view, name="specific-items")
]	