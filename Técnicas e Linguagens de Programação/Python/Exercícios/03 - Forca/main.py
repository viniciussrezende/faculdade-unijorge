from random import choice
from os import system

escolhas = ['PALAVRA', 'OUTRA', 'COMPUTADOR', 'NOVAMENTE', 'FACULDADE']
#escolhas = ['PALAVRA']

palavraEscolhida = choice(escolhas)
palavraEscolhidaModificada = list('-'*len(palavraEscolhida))

acertos = 0
erros = 0


def iniciaJogo():

    print(f"DELETAR POSTERIORMENTE: {palavraEscolhida}")
    letra = input("Digite uma letra: ")
    letra = letra.strip().upper()

    quantidadeContida = palavraEscolhida.count(letra)

    if quantidadeContida > 0:
        if not palavraEscolhidaModificada.count(letra):
            print(f"Possui {quantidadeContida}x na palavra")
            contador = 0
            ocorrencias = []
            for ocorrencia in palavraEscolhida:
                if ocorrencia == letra:
                    ocorrencias.append(contador)
                contador += 1

            contador = 0
            quantidadeOcorrencias = len(ocorrencias)
            while contador < quantidadeOcorrencias:
                palavraEscolhidaModificada[ocorrencias[0]] = letra
                ocorrencias.pop(0)
                contador += 1
            
            
        else:
            print("Você já acertou esta letra!")
    else:
        print("Não está contido!")
        


    input("Aperte ENTER para continuar!")

while True:
    system('cls')
    opcao = input(f"Digite uma das seguintes opções:\n[1] - Nova tentativa;\n[2] - Sair\nPalavra: {palavraEscolhidaModificada}\nACERTOS: {acertos}\nERROS: {erros}\nOpção: ")
    if opcao == '1':
        iniciaJogo()
    elif opcao == '2':
        break
    else:
        print("Opção inválida!")
        input("Aperte ENTER para continuar!")
    

