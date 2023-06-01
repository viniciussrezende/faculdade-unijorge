from random import choice
from os import system

escolhas = ['PALAVRA', 'OUTRA', 'COMPUTADOR', 'NOVAMENTE', 'FACULDADE']

palavraEscolhida = choice(escolhas)
palavraEscolhidaModificada = list('-'*len(palavraEscolhida))

def iniciaJogo():

    







    input("Aperte ENTER para continuar!")

while True:
    system('cls')
    opcao = input(f"Digite uma das seguintes opções:\n[1] - Nova tentativa;\n[2] - Sair\nPalavra: {palavraEscolhidaModificada}\nOpção: ")

    if opcao == '1':
        iniciaJogo()
    elif opcao == '2':
        break
    else:
        print("Opção inválida!")
        input("Aperte ENTER para continuar!")
    

