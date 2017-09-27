#!/usr/bin/python
# -*- coding: utf-8 -*-

class Usuario:

	def __init__(self, codigoUsuario, nomeUsuario):
		self._codigoUsuario = codigoUsuario
		self._nomeUsuario = nomeUsuario

	# Agora ao invés de usar os getters e setters vamos apenas usar a decoração(@)
	@property
	def codigoUsuario(self):
		return self._codigoUsuario

	@codigoUsuario.setter
	def codigoUsuario(self, codigoUsuarioRecebido):
		self._codigoUsuario = codigoUsuarioRecebido

	@property
	def nomeUsuario(self):
		return self._nomeUsuario.upper()

	@nomeUsuario.setter
	def nomeUsuario(self, nomeUsuarioRecebido):
		self._nomeUsuario = nomeUsuarioRecebido

# Fazendo um teste com a classe Usuario...
usuario = Usuario(1, "ronald.falcao")
print(str(usuario.codigoUsuario) + " - " + usuario.nomeUsuario)