from random import choice
from os import system

escolhas = ['PALAVRA', 'OUTRA', 'COMPUTADOR', 'NOVAMENTE', 'FACULDADE']

palavraEscolhida = choice(escolhas)
palavraEscolhidaModificada = list('-'*len(palavraEscolhida))

def iniciaJogo():
    
    print(f"DELETAR POSTERIORMENTE: {palavraEscolhida}")
    letra = input("Digite uma letra: ")
    letra = letra.strip().upper()

    quantidadeContida = palavraEscolhida.count(letra)

    if quantidadeContida > 0:
        print(f"Possui {quantidadeContida}x na palavra")
    else:
        print("Não está contido!")


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
    

