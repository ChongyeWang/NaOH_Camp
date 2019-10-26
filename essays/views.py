from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ImageForm, PostForm
from .models import Post, Images


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
            print(postForm.errors, formset.errors)
    else:
        postForm = PostForm()
        formset = ImageFormSet(queryset=Images.objects.none())
        language = select_language(request)
    return render(request, 'essays.html',
                  {'postForm': postForm, 'formset': formset, 'language': language})


def view_essays(request):
    posts = Post.objects.all()
    language = select_language(request)
    
    context = {
        "posts": posts,
        'language': language    
    }
    return render(request, "view_essays.html", context)


def essay_details(request, pk):
    post = Post.objects.get(pk=pk)
    images = Images.objects.filter(post=post)
    language = select_language(request)
    context = {
       'post': post,
       'images': images,
       'language': language
    }

    return render(request, "essay_details.html", context)


