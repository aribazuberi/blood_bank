from django.shortcuts import render,redirect,get_object_or_404 
from userpage.models import Bank
from userpage.forms import OwnersForm, UpdateForm
from user.models import User


def CreateOwner_view(request):
	context = {}

	user = request.user
	if not user.is_authenticated:
		return redirect("home")

	form = OwnersForm(request.POST)
	if form.is_valid():
		obj = form.save(commit=False)
		owner = User.objects.filter(email=user.email).first()
		obj.owner = owner
		obj.save()
		form = OwnersForm()
		context['createowner_form']=form
		return redirect("ownerpage") 


	return render(request, 'userpage/createowner.html', context) 


def OwnerPage_view(request):
	return render(request, 'userpage/ownerpage.html', {})
  


def UpdateOwner_view(request):
	
	context = {}
	user = request.user
	if not user.is_authenticated:
		return redirect('home')

	
	if request.POST:
		form = UpdateForm(request.POST or None, instance=request.user)
		if form.is_valid():
	
			form = UpdateForm(
				initial={
						#"name": request.POST['name'],
						#"address": request.POST['address'],
						#"contact": request.POST['contact'],
						"A_pos": request.POST['A_pos'],
						"A_neg": request.POST['A_neg'], 
						"B_pos": request.POST['B_pos'],
						"B_neg": request.POST['B_neg'], 
						"O_pos": request.POST['O_pos'],
						"O_neg": request.POST['O_neg'],
						"AB_pos": request.POST['AB_pos'],
						"AB_neg": request.POST['AB_neg'],
					}
				)
			form.save()
			context['success_message'] = "Updated"
		
		context['updateowner_form'] = form

	return render(request, 'userpage/updateowner.html', context) 

	