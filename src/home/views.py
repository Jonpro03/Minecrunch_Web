from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from MinecrunchWeb import settings

# Create your views here.
def index(request):
    
    template = loader.get_template('home/home.html')

    return HttpResponse(template.render())
