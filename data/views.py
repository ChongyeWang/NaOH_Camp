from django.shortcuts import render

def data_analyze(request):
	return render(request, "data_analyze.html", {});

def data_predict(request):
	return render(request, "data_predict.html", {});
