from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView

from .views import HoraView, pizzas_pendentes, cadastro, pedido_pronto, cliente_obs
from .models import Pizza, Cliente

urlpatterns = patterns('',

    #url(r'hora$', hora_atual, name='hora'),
    url(r'hora$', HoraView.as_view(), name='hora'),
    
    #url(r'pizzas$', pizzas_pendentes, name='pizzas'),
    #url(r'pizzas$', ListView.as_view(model=Pizza, context_object_name='lista'), name='lista-pizzas'),
    url(r'pizzas$', ListView.as_view(queryset=Pizza.objects.filter(pedido__pronto=False).order_by('pedido'), 
                                     context_object_name='lista'), 
                                     name='lista-pizzas'),
    
    url(r'clientes$', ListView.as_view(model=Cliente, 
                                       context_object_name='lista'),
                                       name='lista-cliente'),    
    
    url(r'clientes/(?P<pk>\d+)/$', 
        DetailView.as_view(model=Cliente, context_object_name='cliente'), name='ficha-cli'),

    url(r'novocli/$', cadastro, name='cadastro-novo'),
    
    url(r'pedido_pronto/$', pedido_pronto, name='pedido-pronto'),
    
    url(r'cliente_obs/$', cliente_obs, name='cliente-obs'),
    
    
)
