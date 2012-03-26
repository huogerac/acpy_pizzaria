# coding: utf-8

"""
atualiza estrutura de um arquivo json

    >>> updater = DbUpdate('clientes.json')
    >>> updater.read_file()
    >>> updater.show_content()
    [{u'pk': 1, u'model': u'entrega.cliente', u'fields': {u'fone': u'8627 1234', u'email': u'', u'nome': u'Juca'}}]

    >>> updater.addFields((u'ramal', u''))
    >>> updater.addFields((u'logradouro', u''))
    >>> updater.addFields((u'numero', 0))
    >>> updater.addFields((u'complemento', u''))
    >>> updater.addFields((u'obs', u''))
    >>> updater.update_content()
    >>> updater.show_content()
    [{u'pk': 1, u'model': u'entrega.cliente', u'fields': {u'ramal': u'', u'complemento': u'', u'nome': u'Juca', u'fone': u'8627 1234', u'logradouro': u'', u'numero': 0, u'obs': u'', u'email': u''}}]

    >>> updater.save_newfile('clientes_new.json')

"""

import json
import os

class DbUpdate(object):

    def __init__(self, filename):
        self.filename = filename
        self.clientes = []
        self.fields = []
  
    def read_file(self):
        with open(os.path.join(os.path.dirname(__file__), self.filename)) as f:
            self.clientes = json.load(f)

    def addFields(self, newfield):
        self.fields.append(newfield)

    def update_content(self):
        for cliente in self.clientes:
            fields = cliente["fields"]
            for newfield, value in self.fields:
                fields[newfield] = value
    
    def show_content(self):
        print self.clientes

    def save_newfile(self, newfile):
        newcontent = json.dumps(self.clientes, sort_keys=False, indent=4)
        jsonfile = open(newfile, "w")
        jsonfile.write(newcontent)
        jsonfile.close



