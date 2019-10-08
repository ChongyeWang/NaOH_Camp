from django.shortcuts import render
from data.forms import PostForm
from data.models import Content


def select_language(request):
    language = 'English'
    if request.user.is_authenticated:
        if request.session.get(request.user.username, None) == None:
            request.session[request.user.username] = 'Chinese'
        language = request.session[request.user.username]

    return language

def data_analyze(request):
    language = select_language(request)
    context = {
        'language':language
    }
    return render(request, "data_analyze.html", context)


def data_predict(request):
    
    finished = False
    form = PostForm()
    content = Content()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            content= Content(
                q1 = form.cleaned_data["q1"],
                q2 = form.cleaned_data["q2"],
                q3 = form.cleaned_data["q3"],
                q4 = form.cleaned_data["q4"],
            )
            finished = True
            form = PostForm()

    language = select_language(request)

    context = {
        "form": form,
        "contents": content,
        "finished": finished,
        "language": language
    }

    return render(request, "data_predict.html", context);