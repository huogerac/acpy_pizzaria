#!/usr/bin/env python
# coding: utf-8

import json
import argparse
import os

"""
atualiza estrutura de um arquivo json
    
    >>> json = [{'pk': 1, 'model': 'entrega.cliente', 'fields': { 'nome': 'Juca' } }]
    >>> updater = JsonUpdate( json )
    >>> updater.json()
    [{'pk': 1, 'model': 'entrega.cliente', 'fields': {'nome': 'Juca'}}]
    
    >>> updater.addNewField(('ramal', ''))
    >>> updater.updateJson()
    >>> updater.json()
    [{'pk': 1, 'model': 'entrega.cliente', 'fields': {'ramal': '', 'nome': 'Juca'}}]
    
    >>> updater.addNewField(('logradouro', ''))
    >>> updater.addNewField(('numero', 0))
    >>> updater.addNewField(('complemento', ''))
    >>> updater.addNewField(('obs', ''))
    >>> updater.updateJson()
    >>> updater.json()
    [{'pk': 1, 'model': 'entrega.cliente', 'fields': {'ramal': '', 'complemento': '', 'nome': 'Juca', 'logradouro': '', 'numero': 0, 'obs': ''}}]
   
> >> updater.save_newfile('clientes_new.json')

"""



class DbUpdate(object):

    def __init__(self, filename):
        self.filename = filename
  
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

class JsonUpdate(object):

    def __init__(self, json):
        self._json = json
        self._fields = []
        
    def addNewField(self, newfield):
        self._fields.append(newfield)
        
    def updateJson(self):
        for item in self._json:
            fields = item["fields"]
            for newfield, value in self._fields:
                fields[newfield] = value
    
    def json(self):
        return self._json







def update_json(filename, field, value):
    print '-'*60
    print 'atualizando ', filename
    print 'atualizando ', fields
    
    json_content = []
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        json_content = json.load(f)
        
    print json_content
    
    list_fields = fields.split(',')
    print list_fields
    
    updater = JsonUpdate( json )
    updater.addNewField(('ramal', ''))
    
    
    
parser = argparse.ArgumentParser(description='json update')
parser.add_argument('filename', help='file name ex: customer.json')
parser.add_argument('fields', help='fields ex: ("obs","")')

args = parser.parse_args()
update_json(args.filename, args.fields)


