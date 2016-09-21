from django.http import HttpResponse
from django.template import loader
from .models import Player
from django.shortcuts import redirect
from .util.whitelist_form import WhitelistForm


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
