from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from projects.models import Personal_info
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

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


def reset(request):
	if request.user.is_authenticated:
	    if request.method == 'POST':
	        form = PasswordChangeForm(request.user, request.POST)
	        if form.is_valid():
	            user = form.save()
	            update_session_auth_hash(request, user)
	            return redirect('home')
	        
	    else:
	        form = PasswordChangeForm(request.user)
	    return render(request, 'reset.html', {
	        'form': form
	    })
	else:
		
		return register_request(request)


def add_admin(request):
	if request.user.is_superuser:
		if request.method == 'POST':
			form = UserCreationForm(request.POST)
			if form.is_valid():
				form.save()
				username = form.cleaned_data.get('username')
				raw_password = form.cleaned_data.get('password1')
				user = authenticate(username=username, password=raw_password)
				user.is_staff = True
				user.save()

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
		return render(request, 'add_admin.html', {'form': form})
	else:
		return redirect('home')

