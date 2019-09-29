from django.shortcuts import render
from django.db import models
from blog.forms import CommentForm, PostForm
from blog.models import Post, Comment, Category


def blog_index(request):
    # Category.objects.all().delete()
    # Post.objects.all().delete()
    posts = Post.objects.all().order_by('-created_on')
    categories = Category.objects.all()
    context = {
        "posts": posts,
        "categories": categories
    }
    return render(request, "blog_index.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }

    return render(request, "blog_category.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
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

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form
    }

    return render(request, "blog_detail.html", context)


def create_blog(request, category):
    
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

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
        "category": category,
    }

    return render(request, "blog_create.html", context)






