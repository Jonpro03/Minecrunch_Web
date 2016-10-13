from django.contrib.admin import AdminSite
from .util.apply_whitelist_form import ApplyWhitelistForm
import json
from .models.player import Player
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls import url
from django.template.response import TemplateResponse


class WhitelistAdmin(AdminSite):
    site_header = 'Whitelist administration'

    def get_urls(self):
        """Override the get_urls method to inject our own custom, non-model views
        """
        urls = super(WhitelistAdmin, self).get_urls()

        urls += [
            url(r'^apply-whitelist/?$',
                self.admin_view(self.apply_whitelist)),
            url(r'^apply-whitelist-success/?$',
                self.admin_view(self.apply_whitelist_success),
                name='apply_whitelist_success'),
        ]

        return urls

    def apply_whitelist(self, request):
        """Apply Whitelist to Server

        Allows you to apply the latest whitelist information stored on the
        website to the Minecraft server
        """
        form = ApplyWhitelistForm(request)
        context = dict(self.each_context(request))
        context.update({'form': form})

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

                return redirect('apply_whitelist_success')

            except Exception as e:
                context.update({'error': str(e)})

        elif request.method == 'POST':
            context.update({'error': 'Form not valid!'})

        return TemplateResponse(request,
                                'whitelist/apply_whitelist.html',
                                context)

    def apply_whitelist_success(self, request):
        """Indicates that the whitelist was successfully written
        """
        context = dict(self.admin_site.each_context(request))
        return TemplateResponse(request,
                                'apply_whitelist_success.html',
                                context)
