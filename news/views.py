from django.shortcuts import render
from .models import News
from random import shuffle



def select_language(request):
    language = 'English'
    if request.user.is_authenticated:
        if request.session.get(request.user.username, None) == None:
            request.session[request.user.username] = 'Chinese'
        language = request.session[request.user.username]

    return language

def get_all_news(request):
    language = select_language(request)
    news = list(News.objects.all())
    shuffle(news)

    context = {
        'news': news,
        'language': language
    }
    return render(request, "news.html", context)

