from django.shortcuts import render
from django.http import HttpResponse

def home_view(request, *args, **keywordargs):
	return render(request, 'home.html', {})