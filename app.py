# -*- coding UTF-8 -*-

def cadastrar(nomes):
    nome = input("Digite o seu nome: ")
    nomes.append(nome)

def listar(nomes):
    print("Listando os nomes:")
    for nome in nomes:
        print("    ", nome)
    
    print("------------------------------------------------")

def remover(nomes):
    print("Qual nome você gostaria de remover?")
    nome = input()
    if (nome in nomes):
        nomes.remove(nome)
    else:
        print("Nome não encontrado na lista!")

def alterar(nomes):
    print("Qual nome você gostaria de alterar?")
    nome = input()
    if (nome in nomes):
        posicao = nomes.index(nome)
        novo_nome = input("Digite o novo nome: ")
        nomes[posicao] = novo_nome
    else:
        print("Nome não encontrado na lista!")

def procurar(nomes):
    print("Digite o nome a procurar: ")
    nome = input()
    if (nome in nomes):
        print("Nome existente!")
    else:
        print("Nome NÃO existente!")

def menu():
    escolha = ""
    nomes = []
    while (escolha != "0"):
        print("Digite a sua escolha: 1-Cadastrar / 2-Listar / 3-Remover / 4-Alterar / 5-Procurar / 0-Sair")
        escolha = input()

        if (escolha == "1"):
            cadastrar(nomes)
        
        if (escolha == "2"):
            listar(nomes)

        if (escolha == "3"):
            remover(nomes)
        
        if (escolha == "4"):
            alterar(nomes)
        
        if (escolha == "5"):
            procurar(nomes)

    print("Goodbye, and thanks for all the fish.")

menu()