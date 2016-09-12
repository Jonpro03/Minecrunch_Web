from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader
# from MinecrunchWeb import settings


# Create your views here.
def index(request):

    return render(request, 'home/home.html')
