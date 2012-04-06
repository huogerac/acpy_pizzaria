from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView

from .views import HoraView, pizzas_pendentes
from .models import Pizza, Cliente

urlpatterns = patterns('',

    #url(r'hora$', hora_atual, name='hora'),
    url(r'hora$', HoraView.as_view(), name='hora'),
    #url(r'pizzas$', pizzas_pendentes, name='pizzas'),
    url(r'pizzas$', ListView.as_view(model=Pizza, context_object_name='lista')),
    
    url(r'clientes$', ListView.as_view(model=Cliente, context_object_name='lista')),    
    
    url(r'clientes/(?P<pk>\d+)/$', 
        DetailView.as_view(model=Cliente, context_object_name='cliente'), name='ficha-cli'),

)
