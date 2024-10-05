from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/users/login/')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_user(request):
    return render(request, 'users/login.html')