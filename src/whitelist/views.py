from django.http import HttpResponse
from django.template import loader


def index(request):
    """Whitelist Request
    
    Explains the server whitelist policy, and provides a form for applying to be whitelisted
    """

    template = loader.get_template('home/home.html')

    if request.method == 'POST':
        pass

    return HttpResponse(template.render())
