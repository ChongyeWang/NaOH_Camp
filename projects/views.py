from django.shortcuts import render
from projects.models import Personal_info
from blog.models import Post
from essays.models import Post as Column
from videos.models import Post as Video
from videos.models import Videos


def select_language(request):
    language = 'English'
    if request.user.is_authenticated:
        if request.session.get(request.user.username, None) == None:
            request.session[request.user.username] = 'Chinese'
        language = request.session[request.user.username]

    return language


def home(request):

    language = select_language(request)
        
    context = {
        'language': language
    }
    
    return render(request, 'home.html', context)

def setting(request):

    if request.method == 'POST':
        selection = request.POST['selection']
        request.session[request.user.username] = selection

    try:
        user = Personal_info.objects.get(name=request.user.username)
    except:
        user = None
    
    if user == None:
        user = Personal_info(
            name = request.user.username,
            level = 0,
            experience = 0
        )
        user.save()

    level = user.level
    experience = user.experience


    context = {
        'language': request.session[request.user.username],
        'level': level,
        'experience': experience
    }

    return render(request, 'setting.html', context)


def my_post(request):
    posts = Post.objects.filter(
        author=request.user.username
    ).order_by(
        '-created_on'
    )

    language = select_language(request)

    context = {
        'language': language,
        "posts": posts
    }

    return render(request, "my_post.html", context)


def my_column(request):
    posts = Column.objects.filter(
        user=request.user
    ).order_by(
        '-created_on'
    )

    language = select_language(request)

    context = {
        'language': language,
        "posts": posts
    }

    return render(request, "my_column.html", context)


def my_video(request):
    language = select_language(request)

    posts = Video.objects.filter(
        user=request.user
    ).order_by(
        '-created_on'
    )

    result = []
    for post in posts:
        videos = Videos.objects.filter(post=post).get()
        result.append((post, videos))

    context = {
        'language': language,
        "posts": result
    }

    return render(request, "my_video.html", context)


def project_index(request):

    language = select_language(request)
        
    context = {
        'language': language
    }
    return render(request, 'project_index.html', context)


def background(request):
    language = select_language(request)
        
    context = {
        'language': language
    }
    return render(request, 'background.html', context)


def game_setting(request):
    language = select_language(request)
        
    context = {
        'language': language
    } 
    return render(request, 'game_setting.html', context)


def download(request):
    language = select_language(request)
        
    context = {
        'language': language
    }
    return render(request, 'download.html', context)


def map(request):
    language = select_language(request)
        
    context = {
        'language': language
    }
    return render(request, 'map.html', context)


def mod(request):
    language = select_language(request)
        
    context = {
        'language': language
    }
    return render(request, 'mod.html', context)


def history(request):
    language = select_language(request)
        
    context = {
        'language': language
    }

    return render(request, 'history.html', context)


def mission(request):

    language = select_language(request)
        
    context = {
        'language': language
    }

    return render(request, 'mission.html', context)


def mission2(request):

    language = select_language(request)
        
    context = {
        'language': language
    }

    return render(request, 'mission2.html', context)


def unit_data(request):

    language = select_language(request)
        
    context = {
        'language': language
    }

    return render(request, 'unit_data.html', context)





