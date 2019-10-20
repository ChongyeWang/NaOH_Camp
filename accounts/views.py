from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from projects.models import Personal_info
# Create your views here.


def register_request(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)

			person = Personal_info(
				name = request.user.username,
				level = 0,
				experience = 0
			)
			person.save()

			return redirect('home')
	else:
		form = UserCreationForm()
	return render(request, 'signup.html', {'form': form})


def logout_request(request):
     logout(request)
     return redirect('home')