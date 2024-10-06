from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from . import forms

def home(request):
	return render(request, 'pages/home.html')

def about(request):
	return render(request, 'pages/about.html')

def contact(request):
	if request.method == 'POST':
		form = forms.ContactForm(request.POST)
		if form.is_valid():
			massege = form.save(commit=False)
			massege.save()
			return redirect('/')
	else:
		form = forms.ContactForm()
	return render(request, 'pages/contact.html', {'form': form})

def work(request):
	return render(request, 'pages/work.html')

@login_required(login_url='/users/register/')
def skif(request):
	return render(request, 'pages/skif.html')
	