from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone


def get_all_logged_in_users():
    # Query all non-expired sessions
    # use timezone.now() instead of datetime.now() in latest versions of Django
    sessions = Session.objects.filter(expire_date__gte=timezone.now())
    uid_list = []

    # Build a list of user ids from that query
    for session in sessions:
        data = session.get_decoded()
        uid_list.append(data.get('_auth_user_id', None))

    # Query all logged in users based on id list
    return User.objects.filter(id__in=uid_list)


def select_language(request):
    language = 'English'
    if request.user.is_authenticated:
        if request.session.get(request.user.username, None) == None:
            request.session[request.user.username] = 'Chinese'
        language = request.session[request.user.username]

    return language



def index(request):

	language = select_language(request)

	context = {
		'language': language,
		'users': get_all_logged_in_users()
	}
	return render(request, 'chat_index.html', context)


def room(request, room_name):
	user = 'Anonymous: '
	if request.user.is_authenticated:
		user = request.user.username + ': '

	language = select_language(request)

	context = {
		'language': language,
		'room_name_json': mark_safe(json.dumps(room_name)),
		
	}
	return render(request, 'room.html', context)


def all_users(request):
	users = User.objects.all()
	language = select_language(request)
	context = {
		'language': language,
		'users': users
	}
	return render(request, 'all_users.html', context)
