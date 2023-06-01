from random import choice
from os import system


escolhas = ['pedra', 'papel', 'tesoura']

def executaJogo():
    escolhaJogador = input("EscolhaJogador entre pedra, papel e tesoura: ")
    escolhaComputador = choice(escolhas)
    print(f"Computador escolheu: {escolhaComputador}")    
    if escolhaJogador.strip().lower() == escolhas[0]:
        if escolhaComputador == escolhas[0]:
            print("Você empatou!")
        elif escolhaComputador == escolhas[1]:
            print("Você perdeu!")
        else:
            print("Você ganhou!")
    elif escolhaJogador.strip().lower() == escolhas[1]:
        if escolhaComputador == escolhas[0]:
            print("Você ganhou!")
        elif escolhaComputador == escolhas[1]:
            print("Você empatou!")
        else:
            print("Você perdeu!")
    elif escolhaJogador.strip().lower() == escolhas[2]:
        if escolhaComputador == escolhas[0]:
            print("Você perdeu!")
        elif escolhaComputador == escolhas[1]:
            print("Você ganhou!")
        else:
            print("Você empatou!")
    else:
        print("EscolhaJogador inválida!")
    
    input("Aperte ENTER para continuar...")



while True:
    system('cls')
    print("")
    opcao = input("Escolha entre as seguintes opções:\n[1] JOGAR\n[2] SAIR\nOPCÃO: ")

    if opcao.strip().lower() == '1':
        executaJogo()
    elif opcao.strip().lower() == '2':
        break
    else:
        print("Opção inválida!")
        input("Aperte ENTER para continuar...")