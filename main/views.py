from django.shortcuts import render

from userpage.models import Bank

def home_screen_view(request):
	return render(request, "main/home.html", {})


def userhome_view(request):
	context = {}
	banks = Bank.objects.all()
	context['banks'] = banks

	return render(request, "main/userhome.html", context)
