from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def homepage(request):
	context ={
	}
	return render(request,"mainpage/index.html", context)


