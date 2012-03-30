# coding: utf-8
        
from django.contrib import admin
from .models import Cliente, Pedido, Entregador, Pizza

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('fone', 'nome', 'endereco')
    list_display_links = list_display
    search_fields = ['fone', 'nome', 'logradouro']
    list_filter = ('logradouro',)

class PizzaAdmin(admin.TabularInline):
    model = Pizza
    
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('hora_inclusao', 'cliente', 'pronto', 'partiu')
    
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
