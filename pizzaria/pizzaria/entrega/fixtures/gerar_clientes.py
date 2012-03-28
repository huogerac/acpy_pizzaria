# coding: utf-8

'''
[
  {
    "pk": 1, 
    "model": "entrega.cliente", 
    "fields": {
      "ramal": "", 
      "complemento": "", 
      "nome": "Roger", 
      "fone": "86275001", 
      "logradouro": "Teste", 
      "numero": 11, 
      "obs": "", 
      "email": ""
    }
  }
]
'''

from random import randint, choice
import json

LOGRADOUROS = ['Rua Fidalga', 'Rua Girassol', 'Rua Harmonia']

registros = []
for i in range(20):
    campos = dict(ramal='', complemento='', obs='', email='', 
                nome = 'Cliente #%04d' % i, 
                fone = '%4d-%04d' % (randint(2000,4999), randint(0,9999)),
                numero = i + 2000,
                logradouro = choice(LOGRADOUROS) )
    reg = dict(pk=i, model='entrega.cliente', fields=campos)
    registros.append(reg)
    
    
with open('clientela.json', 'wb') as saida:
    json.dump(registros, saida, indent=2)
