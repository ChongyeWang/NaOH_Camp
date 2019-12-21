from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ImageForm, PostForm
from .models import Post, Images
from django.core.paginator import Paginator
from face.models import Face


def select_language(request):
    language = 'English'
    if request.user.is_authenticated:
        if request.session.get(request.user.username, None) == None:
            request.session[request.user.username] = 'Chinese'
        language = request.session[request.user.username]

    return language


@login_required
def essays(request):

    ImageFormSet = modelformset_factory(Images,
                                        form=ImageForm, extra=3)
    #'extra' means the number of photos that you can upload   ^
    language = select_language(request)
    if request.method == 'POST':

        postForm = PostForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Images.objects.none())

        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.user = request.user
            post_form.save()

            for form in formset.cleaned_data:
                #this helps to not crash if the user   
                #do not upload all the photos
                if form:
                    image = form['image']
                    photo = Images(post=post_form, image=image)
                    photo.save()
            messages.success(request,
                             "Success!")
            return HttpResponseRedirect("/essays/view")
        else:
            messages.error(request, 'Invalid Input')
            
    else:
        postForm = PostForm()
        formset = ImageFormSet(queryset=Images.objects.none())
        
    return render(request, 'essays.html',
                  {'postForm': postForm, 'formset': formset, 'language': language})


def view_essays(request):
    language = select_language(request)

    post_list = Post.objects.all()[::-1]
    paginator = Paginator(post_list, 10)

    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    context = {
        "posts": posts,
        'language': language    
    }

    return render(request, "view_essays.html", context)




def essay_details(request, pk):
    post = Post.objects.get(pk=pk)
    images = Images.objects.filter(post=post)

    post.count += 1
    post.save()

    try:
        face = Face.objects.get(name=post.user.username)
    except:
        face = None

    language = select_language(request)
    context = {
       'post': post,
       'images': images,
       'language': language,
       'face': face
    }

    return render(request, "essay_details.html", context)


def one_star(request, pk):
    post = Post.objects.get(pk=pk)
    post.rate_total += 1.0
    post.rate_num += 1
    post.rate = round(post.rate_total / post.rate_num, 1)
    post.save()
    language = select_language(request)
    context = {
       'post': post,
       'language': language
    }
    return render(request, "one_star.html", context)


def two_star(request, pk):
    post = Post.objects.get(pk=pk)
    post.rate_total += 2.0
    post.rate_num += 1
    post.rate = round(post.rate_total / post.rate_num, 1)
    post.save()
    language = select_language(request)
    context = {
       'post': post,
       'language': language
    }
    return render(request, "two_star.html", context)


def three_star(request, pk):
    post = Post.objects.get(pk=pk)
    post.rate_total += 3.0
    post.rate_num += 1
    post.rate = round(post.rate_total / post.rate_num, 1)
    post.save()
    language = select_language(request)
    context = {
       'post': post,
       'language': language
    }
    return render(request, "three_star.html", context)


def four_star(request, pk):
    post = Post.objects.get(pk=pk)
    post.rate_total += 4.0
    post.rate_num += 1
    post.rate = round(post.rate_total / post.rate_num, 1)
    post.save()
    language = select_language(request)
    context = {
       'post': post,
       'language': language
    }
    return render(request, "four_star.html", context)


def five_star(request, pk):
    post = Post.objects.get(pk=pk)
    post.rate_total += 5.0
    post.rate_num += 1
    post.rate = round(post.rate_total / post.rate_num, 1)
    post.save()
    language = select_language(request)
    context = {
       'post': post,
       'language': language
    }
    return render(request, "five_star.html", context)




