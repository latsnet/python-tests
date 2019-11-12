# -*- coding: UTF-8 -*-

class Perfil(object):
    'Classe padrão para perfis de usuários'

    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa

    def imprimir(self):
        print("Nome: %s, Telefone: %s, Empresa: %s" % (self.nome, self.telefone, self.empresa))


class Pessoa(object):

    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = float(peso)
        self.altura = float(altura)

    def imprime(self):
        imc = (self.peso / (self.altura * self.altura))
        print("IMC de %s: %s" % (self.nome, imc))
