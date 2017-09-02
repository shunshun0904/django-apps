from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,'web/home.html',)
# Create your views here.
