from django.contrib import admin
from .util.apply_whitelist_form import ApplyWhitelistForm
import json
from .models.player import Player
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls import url
from django.template.response import TemplateResponse


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

        # Place each player in a dictionary, structured like a whitelist
        # file
        for player in players:
            playerDict = dict()

            playerDict['uuid'] = player.uuid.hex
            playerDict['name'] = player.ign

            whitelist.append(playerDict)

        try:
            # Write the whitelist data to the server's whitelist file
            whitelist_file = open(settings.WHITELIST_FILE, 'w')
            json.dump(whitelist, whitelist_file)

            return redirect('admin:apply_whitelist_success')

        except Exception as e:
            context.update({'error': str(e)})

    elif request.method == 'POST':
        context.update({'error': 'Form not valid!'})

    return TemplateResponse(request,
                            'whitelist/apply_whitelist.html',
                            context)

def apply_whitelist_success(request):
    """Indicates that the whitelist was successfully written
    """
    return TemplateResponse(request,
                            'whitelist/apply_whitelist_success.html',
                            request)


admin.site.register(Player)
admin.site.register_view('apply-whitelist',
                         'Apply Whitelist to Server',
                         view=apply_whitelist)
admin.site.register_view('apply-whitelist-success',
                         visible=False,
                         urlname='apply_whitelist_success',
                         view=apply_whitelist_success)

