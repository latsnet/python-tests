# -*- coding: UTF-8 -*-

class Perfil(object):
    'Classe padrão para perfis de usuários'

    def __init__(self, nome, telefone, empresa):
        if (len(nome) < 10):
            raise ArgumentoInvalido("Nome deve ter pelo menos 10 caracteres")

        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0

    def imprimir(self):
        print("Nome: %s, Telefone: %s, Empresa: %s" % (self.nome, self.telefone, self.empresa))

    def curtir(self):
        self.__curtidas += 1

    def obter_curtidas(self):
        return self.__curtidas

    @classmethod
    def gerar_perfis(classe, nome_arquivo):
        arquivo = open(nome_arquivo, 'r')
        perfis = []
        for linha in arquivo:
            valores = linha.split(',')
            if (len(valores) is not 3):
                raise ValueError("Número de parâmetros inválido")
            
            perfis.append(classe(*valores))
        arquivo.close()
        return perfis

class PerfilVip(Perfil):

    def __init__(self, nome, telefone, empresa, apelido=''):
        super(PerfilVip, self).__init__(nome, telefone, empresa)
        self.apelido = apelido

    def obter_creditos(self):
        return super(PerfilVip, self).obter_curtidas() * 10.0

class Pessoa(object):

    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = float(peso)
        self.altura = float(altura)

    def imprime(self):
        imc = (self.peso / (self.altura * self.altura))
        print("IMC de %s: %s" % (self.nome, imc))

class ArgumentoInvalido(Exception):

    def __init__(self, mensagem):
        self.mensagem = mensagem
    
    def __str__(self):
        return repr(self.mensagem)