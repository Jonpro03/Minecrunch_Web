from django.forms import ModelForm, TextInput
from whitelist.models.player import Player


class WhitelistForm(ModelForm):
    """ Automatically generate a form based on the Player model
    """
    class Meta:
        model = Player
        exclude = ('status',)
        widgets = {
            'ign': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
        }
