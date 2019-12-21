from django.shortcuts import render


def select_language(request):
    language = 'English'
    if request.user.is_authenticated:
        if request.session.get(request.user.username, None) == None:
            request.session[request.user.username] = 'Chinese'
        language = request.session[request.user.username]

    return language


def info_index(request):
	language = select_language(request)
	context = {
		'language': language
	}
	return render(request, "info_index.html", context)


def author_index(request):
	language = select_language(request)
	context = {
		'language': language
	}
	return render(request, "author_index.html", context)


def info_team(request):
	language = select_language(request)
	context = {
		'language': language
	}
	return render(request, "info_team.html", context)


def about_me(request):
	language = select_language(request)
	context = {
		'language': language
	}
	return render(request, "aboutme.html", context);


def ziyuan(request):
	language = select_language(request)
	context = {
		'language': language
	}
	return render(request, "ziyuan.html", context);


