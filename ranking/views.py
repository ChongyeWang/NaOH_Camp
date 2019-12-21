from django.shortcuts import render
from .models import Rating, Comment
from .forms import RankingForm, CommentForm
from django.http import HttpResponseRedirect
from .utils import select_language


def ranking(request):
    ratings = Rating.objects.all().order_by('-rate')

    language = select_language(request)
    context = {
       'ratings': ratings,
       'language': language
    }

    return render(request, "view_ratings.html", context)


def ranking_details(request, pk):
    rating = Rating.objects.get(pk=pk)

    form = CommentForm()

    finished = False

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author = request.user,
                body = form.cleaned_data["body"],
                rating = rating
            )
            comment.save()
            form = CommentForm()

            finished = True

    comments = Comment.objects.filter(rating=rating)

    language = select_language(request)

    context = {
        "comments": comments,
        "form": form,
        "language": language,
        "finished": finished,
        'rating': rating,
    }

    return render(request, "rating_details.html", context)



def post_ranking(request):

    language = select_language(request)

    rankingForm = RankingForm(request.POST)

    if request.method == 'POST':

        rankingForm = RankingForm(request.POST)
        
        if rankingForm.is_valid():

            name = rankingForm.cleaned_data["name"]

            try:
            	rating = Rating.objects.get(name=name)
            except:
            	rating = None

            if rating == None:
            
	            rating = Rating(
	                name = rankingForm.cleaned_data["name"],
	                body = rankingForm.cleaned_data["body"],
	            )
	            rating.save()

            else:
                
                c_punc = ' 。， ？《》，！@#¥%……'
                e_punc = '!#$%&()*+, -./:;<=>?@[]^_`{|}~'

                last = rating.body[len(rating.body) - 1]

                if last in c_punc or last in e_punc:
                	rating.body += rankingForm.cleaned_data["body"]
                else:
                	rating.body += (' ' + rankingForm.cleaned_data["body"])

                rating.save()

            return HttpResponseRedirect("/ranking/")

        
    return render(request, 'rating_post.html',
                  {'rankingForm': rankingForm, 'language': language})




def one_star(request, pk):
    rating = Rating.objects.get(pk=pk)
    rating.rate_total += 1.0
    rating.rate_num += 1
    rating.rate = round(rating.rate_total / rating.rate_num, 1)
    rating.save()
    language = select_language(request)

    context = {
       'rating': rating,
       'language': language
    }
    return render(request, "r_one_star.html", context)


def two_star(request, pk):
    rating = Rating.objects.get(pk=pk)
    rating.rate_total += 2.0
    rating.rate_num += 1
    rating.rate = round(rating.rate_total / rating.rate_num, 1)
    rating.save()
    language = select_language(request)
    context = {
       'rating': rating,
       'language': language
    }
    return render(request, "r_two_star.html", context)


def three_star(request, pk):
    rating = Rating.objects.get(pk=pk)
    rating.rate_total += 3.0
    rating.rate_num += 1
    rating.rate = round(rating.rate_total / rating.rate_num, 1)
    rating.save()
    language = select_language(request)
    context = {
       'rating': rating,
       'language': language
    }
    return render(request, "r_three_star.html", context)


def four_star(request, pk):
    rating = Rating.objects.get(pk=pk)
    rating.rate_total += 4.0
    rating.rate_num += 1
    rating.rate = round(rating.rate_total / rating.rate_num, 1)
    rating.save()
    language = select_language(request)
    context = {
       'rating': rating,
       'language': language
    }
    return render(request, "r_four_star.html", context)


def five_star(request, pk):
    rating = Rating.objects.get(pk=pk)
    rating.rate_total += 5.0
    rating.rate_num += 1
    rating.rate = round(rating.rate_total / rating.rate_num, 1)
    rating.save()
    language = select_language(request)
    context = {
       'rating': rating,
       'language': language
    }
    return render(request, "r_five_star.html", context)

