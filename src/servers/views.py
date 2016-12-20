from django.shortcuts import get_object_or_404, render
from .models import Server


def index(request):
    '''
    Display a list of any and all servers in the Minecrunch network
    '''

    servers = Server.objects.all()

    return render(request, 'servers/servers.html', {'servers': servers})


def server(request, slug):
    '''
    A detailed description of a single server, including a dynmap window
    '''

    server = get_object_or_404(Server, slug=slug)

    return render(request, 'servers/server.html', {'server': server})

