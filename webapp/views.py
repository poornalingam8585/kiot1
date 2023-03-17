from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
	obj = userdetails.objects.all()
	if request.method == "POST":
		if request.POST['form_name'] == "contactform":
			userdetails(name = request.POST['name'],email = request.POST['email'],subject= request.POST['subject']).save()
			messages.success(request,"userdetails added Successfully!")
			return redirect('index')
	return render(request,"index.html",locals())
