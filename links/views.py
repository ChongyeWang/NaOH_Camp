from django.shortcuts import render
from .models import Link
from .forms import LinkForm
from django.http import HttpResponseRedirect
from .utils import select_language

def get_all_links(request):
    links = Link.objects.all()[::-1]

    links1 = []
    links2 = []

    for i in range(len(links)):
        if i % 2 == 0:
        	links1.append(links[i])
        else:
        	links2.append(links[i])
        print(links[i].link)

    language = select_language(request)



    context = {
       'links1': links1,
       'links2': links2,
       'language': language
    }

    return render(request, "view_links.html", context)

def upload_link(request):

    language = select_language(request)

    linkForm = LinkForm()

    if request.method == 'POST':

        linkForm = LinkForm(request.POST)
        
        if linkForm.is_valid():

            link = Link(
                name = linkForm.cleaned_data["name"],
                link = linkForm.cleaned_data["link"],
            )
            link.save()

            return HttpResponseRedirect("/links/")

        
    return render(request, 'link_post.html',
                  {'linkForm': linkForm, 'language': language})

