from django.shortcuts import render
from django.http import HttpResponse
from . import templates


# Create your views here.
def new_user(request):

	return render(request, 'email_id_collection/sign_up_page.html')
	# return HttpResponse("Hi I am shiv")
