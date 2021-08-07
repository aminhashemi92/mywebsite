from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
# Create your views here.
from .forms import *

def python_course(request):
	context ={
	}
	return render(request,"course/course_main.html", context)
	# return HttpResponse("hi")


def register(request):
	form = MemberForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = MemberForm()
		return redirect('/')

	context = {'form':form}
	return render(request,"course/register.html", context)
	# return HttpResponse("hi")

