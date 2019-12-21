from django.shortcuts import render
from projects.models import Personal_info
from blog.models import Post
from essays.models import Post as Column
from videos.models import Post as Video
from videos.models import Videos

from .utils import select_language

from face.models import Face


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

    try:
        face = Face.objects.get(name=request.user.username)
    except:
        face = None

    context = {
        'language': request.session[request.user.username],
        'level': level,
        'experience': experience,
        'face': face
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


def story(request):

    language = select_language(request)
        
    context = {
        'language': language
    }

    return render(request, 'story.html', context)


def super_weapon(request):

    language = select_language(request)
        
    context = {
        'language': language
    }

    return render(request, 'super_weapon.html', context)


def tech_building(request):

    language = select_language(request)
        
    context = {
        'language': language
    }

    return render(request, 'tech_building.html', context)


def timeline(request):

    language = select_language(request)
        
    context = {
        'language': language
    }

    return render(request, 'timeline.html', context)


def quotes(request):

    language = select_language(request)
        
    context = {
        'language': language
    }

    return render(request, 'quotes.html', context)


def manual1(request):

    language = select_language(request)
        
    context = {
        'language': language
    }

    return render(request, 'manual1.html', context)


def manual2(request):

    language = select_language(request)
        
    context = {
        'language': language
    }

    return render(request, 'manual2.html', context)



def stat(request):

    language = select_language(request)
        
    context = {
        'language': language
    }

    return render(request, 'stat.html', context)


def time(request):

    language = select_language(request)
        
    context = {
        'language': language
    }

    return render(request, 'time.html', context)


def special(request):

    language = select_language(request)
        
    context = {
        'language': language
    }

    return render(request, 'special.html', context)


def yuri(request):

    language = select_language(request)
        
    context = {
        'language': language
    }

    return render(request, 'yuri.html', context)
