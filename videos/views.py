from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import PostForm, VideoForm
from .models import Post, Videos
from django.core.paginator import Paginator


def select_language(request):
    language = 'English'
    if request.user.is_authenticated:
        if request.session.get(request.user.username, None) == None:
            request.session[request.user.username] = 'Chinese'
        language = request.session[request.user.username]

    return language


@login_required
def videos(request):

    language = select_language(request)

    if request.method == 'POST':

        postForm = PostForm(request.POST)
        videoForm = VideoForm(request.POST, request.FILES)

        if postForm.is_valid() and videoForm.is_valid():
            post_form = postForm.save(commit=False)
            post_form.user = request.user
            post_form.save()

            videos = videoForm.cleaned_data['video']
            video = Videos(post=post_form, video=videos)
            video.save()

            messages.success(request,
                             "Success!")
            return HttpResponseRedirect("/videos/view")
        else:
            messages.error(request, 'Maximum Word Limit Exceeded')
    else:
        postForm = PostForm()
        videoForm = VideoForm()
    return render(request, 'videos.html',
                  {'postForm': postForm, 'videoForm': videoForm, 'language': language})


def view_videos(request):

    result = []
    posts = Post.objects.all()
    for post in posts:
        videos = Videos.objects.filter(post=post).get()
        result.append((post, videos))

    language = select_language(request)


    paginator = Paginator(result, 12)

    page = request.GET.get('page')
    result = paginator.get_page(page)
    
    context = {
        "posts": result,
        'language': language,
    }

    return render(request, "view_videos.html", context)



def video_search(request):

    search_result = request.GET['search_result']
    print(search_result)

    empty = False
    if not search_result:
        empty = True

    posts = Post.objects.filter(
        body__contains=search_result
    ).order_by(
        '-created_on'
    )

    result = []

    for post in posts:
        videos = Videos.objects.filter(post=post).get()
        result.append((post, videos))


    if len(posts) == 0:
        empty = True

    language = select_language(request)

    context = {
        "empty": empty,
        "posts": result,
        "language": language
    }

    return render(request, "video_search_result.html", context)


