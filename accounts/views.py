from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .forms import RegisterAccountForm


def account_register_view(request):
	form = RegisterAccountForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = RegisterAccountForm()

	context={'form' : form}
	return render(request, 'accounts/register.html', context)

def account_login_view(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)

		if user is None:
			login(request, user)
			return redirect('')

	context={}
	return render(request, 'accounts/login.html', context)

def account_home_view(request):
	context={}
	return render(request, 'accounts/accounts_home.html', context)
	