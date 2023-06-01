from random import choice
from os import system

escolhas = ['PALAVRA', 'OUTRA', 'COMPUTADOR', 'NOVAMENTE', 'FACULDADE']
#escolhas = ['PALAVRA']

palavraEscolhida = choice(escolhas)
palavraEscolhidaModificada = list('-'*len(palavraEscolhida))

resultado = [0 , 0]
corpo = ''
#
# resultado = [ ACERTOS, ERROS  ]




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
                resultado[0] += 1
            
            
            
        else:
            print("Você já acertou esta letra!")
    else:
        print("Não está contido!")
        resultado[1] += 1

    input("Aperte ENTER para continuar!")

while True:
    system('cls')
    opcao = input(f"Digite uma das seguintes opções:\n[1] - Nova tentativa;\n[2] - Sair\nPalavra: {palavraEscolhidaModificada}\nACERTOS: {resultado[0]}\nERROS: {resultado[1]}\n{corpo}\nOpção: ")
    if opcao == '1':
        iniciaJogo()
    elif opcao == '2':
        break
    else:
        print("Opção inválida!")
        input("Aperte ENTER para continuar!")
        
    if resultado[1] == 1:
        corpo = "()"
    elif resultado[1] == 2:
        corpo = " ()\n/"     
    elif resultado[1] == 3:
        corpo = " ()\n/  \\"
    elif resultado[1] == 4:
        corpo = " ()\n/|\\\n"
    elif resultado[1] == 5:
        corpo = " ()\n/|\\\n/"
    elif resultado[1] == 6:
        corpo = " ()\n/|\\\n/ \\"    

