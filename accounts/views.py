from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def account_register_view(request):
	form = UserCreationForm()
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
	context={'form' : form}
	return render(request, 'accounts/register.html', context)

def account_login_view(request):
	context={}
	return render(request, 'accounts/login.html', context)

def account_home_view(request):
	context={}
	return render(request, 'accounts/accounts_home.html', context)
	