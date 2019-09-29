from django.shortcuts import render


def info_index(request):
	return render(request, "info_index.html", {});

def author_index(request):
	return render(request, "author_index.html", {});