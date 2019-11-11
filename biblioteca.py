def gera_nome_convite(convite):
    posicao_final = len(convite)
    posicao_inicial = posicao_final - 4
    parte1 = convite[0:4]
    parte2 = convite[posicao_inicial:posicao_final]
    return parte1 + ' ' + parte2

def envia_convite(convite):
    print('Enviando convite para %s' % (convite))

def processa_convite(convite):
    nome_formatado = gera_nome_convite(convite)
    envia_convite(nome_formatado)

def calcula_idade():
    ano_como_string = input("Digite o ano do seu nascimento: ")
    ano_como_int = int(ano_como_string)
    print("Sua idade é %s anos " % (2019 - ano_como_int))

def cadastrar(nomes):
    nome = input("Digite o seu nome: ")
    nomes.append(nome)

def remover(nomes):
    print("Qual nome você gostaria de remover?")
    nome = input()
    nomes.remove(nome)
