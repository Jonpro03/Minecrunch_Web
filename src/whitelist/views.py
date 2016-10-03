from django.http import HttpResponse
from django.template import loader
from .models.player import Player
from django.shortcuts import redirect
from .util.whitelist_form import WhitelistForm
from .util.apply_whitelist_form import ApplyWhitelistForm

import json
from django.conf import settings
from django.template.response import TemplateResponse
# from django.contrib.sites import requests


def index(request):
    """Whitelist Request

    Explains the server whitelist policy, and provides a form for applying to
    be whitelisted
    """

    player = Player()

    # Handle a request to be whitelisted
    if request.method == 'POST':
        form = WhitelistForm(request.POST, instance=player)

        if form.is_valid():
            player.save()
            return redirect('submitted')
    else:
        form = WhitelistForm()

    template = loader.get_template('whitelist/index.html')

    return HttpResponse(template.render({'form': form}, request))


def apply_whitelist(request):
    """Apply Whitelist to Server

    Allows you to apply the latest whitelist information stored on the
    website to the Minecraft server
    """
    form = ApplyWhitelistForm(request)
    context = {'form': form}

    # Handle a request to be whitelisted
    if request.method == 'POST' and form.is_valid():
        players = Player.objects.filter(status=Player.APPROVED)
        whitelist = []

        # Place each player in a dictionary, structured like a whitelist file
        for player in players:
            playerDict = dict()

            playerDict['uuid'] = player.uuid.hex
            playerDict['name'] = player.ign

            whitelist.append(playerDict)

        try:
            # Write the whitelist data to the server's whitelist file
            whitelist_file = open(settings.WHITELIST_FILE, 'w')
            json.dump(whitelist, whitelist_file)

            return redirect('apply_whitelist_success')

        except Exception as e:
            context.update({'error': str(e)})
            # context = context + {'error': error}
    elif request.method == 'POST':
        context.update({'error': 'Form not valid!'})

    return TemplateResponse(request,
                            'whitelist/apply_whitelist.html',
                            context)


def apply_whitelist_success(request):
    """Indicates that the whitelist was successfully written
    """
    return TemplateResponse(request, 'whitelist/apply_whitelist_success.html')
