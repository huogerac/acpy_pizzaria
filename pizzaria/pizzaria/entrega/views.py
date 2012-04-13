# coding: utf-8
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
import datetime

from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse

from .models import Pizza
from .forms import ClienteModelForm

#nao utilizado
def hora_atual_na_unha(request):
    agora = datetime.datetime.now()
    html = '<html><h1> Hora: {0}</h1></html>'.format(agora)
    return HttpResponse(html)
    
#nao utilizado    
def pizzas_pendentes_na_unha(request):
    listagem = []
    for pizza in Pizza.objects.all():
        listagem.append(unicode(pizza))
    listagem = u'\n'.join(listagem)

    html = u'<html><body><h1>Pizzas pendentes</h1>'
    html += u'<pre>{0}</pre></body></html>'.format(listagem)

    return HttpResponse(html)
    
    
class HoraView(TemplateView):
    template_name = 'entrega/hora.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(HoraView, self).get_context_data(**kwargs)
        context['hora_certa'] = datetime.datetime.now()
        return context






def pizzas_pendentes(request):

    lista_de_pizzas = Pizza.objects.all()
    
    return render(request, 'entrega/pizzas.html', 
        {"lista": lista_de_pizzas},
        content_type="text/html")



def cadastro(request):
    if request.method == 'POST':
        formulario = ClienteModelForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            #TODO: usar reverse 
            #return HttpResponseRedirect('/ent/clientes')
            return HttpResponseRedirect(reverse('lista-cliente'))
    else:
        formulario = ClienteModelForm()
        
    return render(request, 'entrega/cadastro.html',
                  {'formulario': formulario})
        