from django.shortcuts import render
from django.db import models
from blog.forms import CommentForm, PostForm
from blog.models import Post, Comment, Category
from django.contrib.auth.models import User
from projects.models import Personal_info

def select_language(request):
    language = 'English'
    if request.user.is_authenticated:
        if request.session.get(request.user.username, None) == None:
            request.session[request.user.username] = 'Chinese'
        language = request.session[request.user.username]

    return language

def blog_index(request):
    # Category.objects.all().delete()
    # Post.objects.all().delete()
    posts = Post.objects.all().order_by('-created_on')
    size = Category.objects.all().count()
    categories1 = Category.objects.all()[:size/2]
    categories2 = Category.objects.all()[size/2:]

    language = select_language(request)
    user_num = User.objects.all().count()

    context = {
        "posts": posts,
        "categories1": categories1,
        "categories2": categories2,
        "language": language,
        "user_num": user_num,
    }
    return render(request, "blog_index.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )

    language = select_language(request)

    order = 'reverseorder'
    if request.method == 'POST':
        order = request.POST['selection']

    if order == 'inorder':
        posts = posts[::-1]

    context = {
        "category": category,
        "posts": posts,
        "language": language,
        "order": order
    }

    return render(request, "blog_category.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()

    finished = False

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author = request.user,
                body = form.cleaned_data["body"],
                post = post
            )
            comment.save()
            form = CommentForm()

            finished = True

    comments = Comment.objects.filter(post=post)
    language = select_language(request)

    context = {
        "post": post,
        "comments": comments,
        "form": form,
        "language": language,
        "finished": finished
    }

    return render(request, "blog_detail.html", context)


def create_blog(request, category):

    finished = False
    
    form = PostForm(request.POST)
    post = Post()
    if request.method == 'POST':
        if form.is_valid():
            post = Post(
                title = form.cleaned_data["title"],
                author = request.user,
                body = form.cleaned_data["body"],
            )
            post.save()
            post.created_on = models.DateTimeField(auto_now_add=True)
            post.last_modified = models.DateTimeField(auto_now=True)
            curr_category = Category.objects.get(name=category)
            post.categories.add(curr_category)

            finished = True

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

            user = Personal_info.objects.get(name=request.user.username)
            user.experience += 100
            user.level = int(user.experience / 500)
            user.save()

    comments = Comment.objects.filter(post=post)
    language = select_language(request)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
        "category": category,
        "language": language,
        "finished": finished
    }

    return render(request, "blog_create.html", context)


def blog_search(request):

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

    if len(posts) == 0:
        empty = True

    language = select_language(request)

    context = {
        "empty": empty,
        "posts": posts,
        "language": language
    }

    return render(request, "search_result.html", context)


