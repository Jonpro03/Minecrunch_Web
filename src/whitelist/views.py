from django.http import HttpResponse
from django.template import loader
from .models import Player
from django.shortcuts import redirect
from django.contrib.sites import requests
from .whitelist_form import WhitelistForm


def index(request):
    """Whitelist Request

    Explains the server whitelist policy, and provides a form for applying to
    be whitelisted
    """

    player = Player()
    form = WhitelistForm(request.POST, instance=player)

    # Handle a request to be whitelisted
    if request.method == 'POST' and form.is_valid():
        player.save()
        return redirect('whitelist:submitted')

    template = loader.get_template('whitelist/index.html')

    return HttpResponse(template.render({'form': form}))
