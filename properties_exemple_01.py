#!/usr/bin/python
# -*- coding: utf-8 -*-

# Fazendo o uso tradicional de get's e set's comumente utilizados em JAVA, C++, etc.

class Usuario:

	# Setando os valores dos atributos com os respectivos métodos set()... 
    def __init__(self,codigoUsuario, nomeUsuario):
        self.setCodigoUsuario(codigoUsuario)
        self.setNomeUsuario(nomeUsuario)

    def getCodigoUsuario(self):
    	return self.codigoUsuario

    def setCodigoUsuario(self, codigoUsuario):
    	self.codigoUsuario = codigoUsuario
    
    def getNomeUsuario(self):
    	return self.nomeUsuario.upper()

    def setNomeUsuario(self, nomeUsuario):
    	self.nomeUsuario = nomeUsuario

# Fazendo um teste com a classe...
usuario = Usuario(1,"ronald.falcao")
print(str(usuario.getCodigoUsuario()) + " - " + usuario.getNomeUsuario())

