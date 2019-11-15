from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from user.forms import RegistrationForm,UserAuthenticationForm,AccountUpdateForm
from django.http import HttpResponse


def registration_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user=form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			#user = authenticate(email=email, password=raw_password)
			login(request, user)
			return redirect("home")
		else:
			context['registration_form']=form
	else:
		form = RegistrationForm()
		context['registration_form']=form

	return render(request, 'user/register.html', context)

def logout_view(request):
	logout(request)
	return redirect('home')


def login_view(request):

	 context = {}

	 user = request.user
	 print('!!!!!!!!!!!!', user.is_authenticated)
	 if user.is_authenticated:
	 	return redirect('home')

	 if request.POST:
	 	form = UserAuthenticationForm(request.POST)
	 	if form.is_valid():
	 		email = request.POST['email']
	 		password = request.POST['password']
	 		user = authenticate(email=email, password=password)

	 		if user:
	 			login(request, user)
	 			return redirect('home')

	 else:
	 	form =UserAuthenticationForm()

	 context['login_form'] = form
	 return render(request, 'user/login.html', context)



def update_view(request):

	if not request.user.is_authenticated:
		return redirect('login')

	context = {}

	if request.POST:
		form = AccountUpdateForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
	else:
		form = AccountUpdateForm(
				initial= {
					"email": request.user.email,
					"username": request.user.username,
				}
			)
	context['update_form'] = form
	return render(request, 'user/update.html', context)


 



def home(request):
    return HttpResponse('<h1>User Home</h1>')


def profile(request):
    return HttpResponse('<h1>User Profile</h1>')