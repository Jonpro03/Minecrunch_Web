from django.forms import ModelForm
from whitelist.models import Player


class WhitelistForm(ModelForm):
    """ Automatically generate a form based on the Player model
    """
    class Meta:
        model = Player
        fields = ('ign', 'email')
