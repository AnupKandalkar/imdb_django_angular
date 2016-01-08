# Create your views here.
from django.views.generic import ListView
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext


def home(request):
	return render_to_response("index.html",{},RequestContext(request))