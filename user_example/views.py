from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def index(request):
	return render(request, 'user_example/index.html')


def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('index')
	else:
		form = UserCreationForm()
	context = {'form': form}
	return render(request, 'registration/register.html', context)

def blog(request):
	if not request.user.is_authenticated:
		return render(request, 'user_example/error.html')
	else:
		return render(request, 'user_example/blog.html')

@login_required(login_url='/accounts/login/')
def blog2(request):
	return render(request, 'user_example/blog2.html')
#