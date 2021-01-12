from django.urls import path
from django.contrib import admin
from . import views

app_name="ocrreader"

urlpatterns = [
	path('upload', views.upload_view, name='upload'),
]