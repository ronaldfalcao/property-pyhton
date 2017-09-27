#!/usr/bin/python
# -*- coding: utf-8 -*-

class Usuario:

	def __init__(self, codigoUsuario, nomeUsuario):
		self._codigoUsuario = codigoUsuario
		self._nomeUsuario = nomeUsuario

	def getCodigoUsuario(self):
		return self._codigoUsuario

	def setCodigoUsuario(self, codigoUsuario):
		self._codigoUsuario = codigoUsuario

	def getNomeUsuario(self):
		return self._nomeUsuario.upper()

	def setNomeUsuario(self, nomeUsuario):
		self._nomeUsuario = nomeUsuario

	# Definição das properties, mas ainda com o uso de set's e get's...
	codigoUsuario = property(fget=getCodigoUsuario, fset=setCodigoUsuario)
	nomeUsuario = property(fget=getNomeUsuario, fset=setNomeUsuario)

# Fazendo um teste com a classe Usuario, prestar atenção que o próprio Python lidou
# com as referências de get's e set's sem a necessidade de explicitamente serem
# convocados os métodos...
usuario = Usuario(1, "ronald.falcao")
print(str(usuario.codigoUsuario) + " - " + usuario.nomeUsuario)