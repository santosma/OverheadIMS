from django.urls import path
from . import views

app_name='accounts'

urlpatterns = [
	path('register/', views.account_register_view, name='account-register'),
	path('login/', views.account_login_view, name='account-login'),
	path('', views.account_home_view, name='accounts-info'),
]