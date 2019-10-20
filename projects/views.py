from django.shortcuts import render

from projects.models import Personal_info


def select_language(request):
    language = 'English'
    if request.user.is_authenticated:
        if request.session.get(request.user.username, None) == None:
            request.session[request.user.username] = 'Chinese'
        language = request.session[request.user.username]

    return language


def home(request):

    language = 'English'
    if request.user.is_authenticated:
        if request.session.get(request.user.username, None) == None:
            request.session[request.user.username] = 'Chinese'
        language = request.session[request.user.username]
        
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

# def project_detail(request, pk):
#     project = Project.objects.get(pk=pk)
#     language = 'English'
#     if request.user.is_authenticated:
#         if request.session.get(request.user.username, None) == None:
#             request.session[request.user.username] = 'Chinese'
#         language = request.session[request.user.username]
#     context = {
#         'project': project,
#         'language': language
#     }
#     return render(request, 'project_detail.html', context)