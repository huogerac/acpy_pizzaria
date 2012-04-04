# Create your views here.

from django.http import HttpResponse
import datetime

def hora_atual(request):

    agora = datetime.datetime.now()
    html = '<html><h1> Hora: {0}</h1></html>'.format(agora)
    #html = '<html><h1>' + str(agora) + '</h1></html>'

    return HttpResponse(html)

