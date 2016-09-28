from django.http import HttpResponse
from django.template import loader
from .models.player import Player
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from .util.whitelist_form import WhitelistForm
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


@staff_member_required
def applyWhitelist(request):
    """Apply Whitelist to Server

    Allows you to apply the latest whitelist information stored on the website
    to the Minecraft server
    """

    players = Player.objects.filter(status=Player.APPROVED)
    whitelist = []

    for player in players:
        playerDict = {}
        playerDict['uuid'] = player.uuid
        playerDict['name'] = player.ign

        whitelist.append(playerDict)

    # try:
    #    pass
    # except Exception e:
    #    pass
