#!/usr/bin/python
# -*- coding: utf-8 -*-

# Como não temos nenhuma valiação podemos resumir toda a implementação no
# construtor da classe (com ressalvas!!!)

class Usuario:

    def __init__(self,codigoUsuario, nomeUsuario):
        self.codigoUsuario = codigoUsuario
        self.nomeUsuario = nomeUsuario.upper()
        

usuario = Usuario(1,"ronald.falcao")
print(str(usuario.codigoUsuario) + " - " + usuario.nomeUsuario)

