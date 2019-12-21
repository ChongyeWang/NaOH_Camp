from django.shortcuts import render
from .models import Face
from django.templatetags.static import static

from django.http import HttpResponseRedirect
from .forms import Photo
from .utils import select_language



def face_upload(request):

	if request.user.is_authenticated:
		language = select_language(request)
		image_form = Photo()

		if request.method == 'POST':
			image_form = Photo(request.POST, request.FILES)       
			if image_form.is_valid():
				try:
					curr_user = Face.objects.get(name=request.user.username)
				except:
					curr_user = None
				if curr_user == None:
					face = Face(
						name = request.user.username,
						image = image_form.cleaned_data["image"]
					)
					face.save()
				else:
					curr_user.image = image_form.cleaned_data["image"]
					curr_user.save()
				return HttpResponseRedirect("/setting/")

		try:
			face = Face.objects.get(name=request.user.username)
		except:
			face = None

		return render(request, "face.html", {'image_form': image_form, 'language': language, 'face': face})

	else:
		return HttpResponseRedirect("/accounts/login/")
