from django.http import HttpResponse
# from django.shortcuts import render
from django.template import loader
from modpacks.models import Modpack  # , mod
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound


def index(request):
    '''
    Lists all available modpacks
    '''

    modpacks = Modpack.objects.all()
    template = loader.get_template('modpacks/modpacks.html')

    return HttpResponse(template.render({'modpacks': modpacks}))


def modpack(request, slug):
    '''
    Displays a modpack's details, including available mods and description of
    the overall modpack
    Note: Currently unimplemented
    '''
    modpack = Modpack.objects.filter(slug=slug)

    if not modpack.exists():
        raise HttpResponseNotFound('No modpack matching that slug')

    template = loader.get_template('home/modpack.html')

    return HttpResponse(template.render(modpack))
