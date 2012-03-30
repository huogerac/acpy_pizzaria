# coding: utf-8
        
from django.contrib import admin
from django.db.models import TextField
from django.forms import Textarea

from .models import Cliente, Pedido, Entregador, Pizza

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('fone', 'nome', 'endereco')
    list_display_links = list_display
    search_fields = ['fone', 'nome', 'logradouro']
    list_filter = ('logradouro',)

class PizzaAdmin(admin.TabularInline):
    model = Pizza
    #exclude = ('obs',)
    formfield_overrides = {
        TextField: { 'widget': Textarea(attrs={'rows':2, 'cols':20})}, 
    }
    
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('hora_inclusao', 'cliente', 'pronto', 'partiu')
    #faz contem o django faça join para evitar selects desnecessários
    #como é o caso do cliente (campos do __unicode__)
    list_select_related = True
    
    #mostra o filtro por data no topo
    date_hierarchy = 'inclusao'
        
    def hora_inclusao(self, obj):
        return obj.inclusao.strftime('%HH:%MM')
    
    def partiu(self, obj):
        return bool(obj.pronto and obj.entregador and obj.partida)
    partiu.boolean = True
    
    inlines = [PizzaAdmin]

    
    
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Entregador)
#admin.site.register(Pizza)
