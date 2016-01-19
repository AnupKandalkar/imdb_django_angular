# Create your views here.
from django.views.generic import ListView
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext


def home(request):
	usertype = request.user.is_superuser
	if request.user.is_authenticated():
		print "authentication"
	else:
		print "unauthentication"
	# print "requerie ",request.user.is_authentication
	return render_to_response("index.html",{"usertype":usertype},RequestContext(request))