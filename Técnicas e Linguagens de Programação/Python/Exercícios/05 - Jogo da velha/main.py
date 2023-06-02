from os import system

matrizImpressao = [[' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' ']]

matrizJogo = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

quantidadeJogada = 0

ganhador = [0, 0]

def resetaJogo():
    matrizImpressao = [[' ', ' ', ' '],
                       [' ', ' ', ' '],
                       [' ', ' ', ' ']]

    matrizJogo = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]

    quantidadeJogada = 0

def imprime():
    print(" -----------")
    print("| {0} | {1} | {2} |".format(matrizImpressao[0][0], matrizImpressao[0][1], matrizImpressao[0][2]))
    print(" -----------")
    print("| {0} | {1} | {2} |".format(matrizImpressao[1][0], matrizImpressao[1][1], matrizImpressao[1][2]))
    print(" -----------")
    print("| {0} | {1} | {2} |".format(matrizImpressao[2][0], matrizImpressao[2][1], matrizImpressao[2][2]))
    print(" -----------")

def verificaGanhador():
    for i in range(3):
        verificacaoJogo = 0
        for j in range(3):
            verificacaoJogo += matrizJogo[i][j]
            if verificacaoJogo == 3:
                ganhador[0] = 1
                resetaJogo()
            elif verificacaoJogo == -3:
                ganhador[1] = 1
                resetaJogo()
    verificacaoJogo = 0

    for i in range(3):
        verificacaoJogo = 0
        for j in range(3):
            verificacaoJogo += matrizJogo[j][i]
            if verificacaoJogo == 3:
                ganhador[0] = 1
                resetaJogo()
            elif verificacaoJogo == -3:
                ganhador[1] = 1
                resetaJogo()
    verificacaoJogo = 0

    for i in range(3):
        for j in range(3):
            if j == i:
                verificacaoJogo += matrizJogo[j][i]
                if verificacaoJogo == 3:
                    ganhador[0] = 1
                    resetaJogo()
                elif verificacaoJogo == -3:
                    ganhador[1] = 1
                    resetaJogo()
    
    verificacaoJogo = 0
    for i in range(3):
        for j in range(3):
            if (j == 2 and i == 0) or (j == 1 and i == 1) or (j == 0 and i == 2):
                verificacaoJogo += matrizJogo[j][i]
                if verificacaoJogo == 3:
                    ganhador[0] = 1
                    resetaJogo()
                elif verificacaoJogo == -3:
                    ganhador[1] = 1
                    resetaJogo()
   


def iniciaJogo():
    global quantidadeJogada

    if quantidadeJogada % 2 == 0:
        while True:
            linha = int(input("Jogador 1 digite a linha que você quer colocar o X: "))
            coluna = int(input("Jogador 1 digite a coluna que você quer colocar o X: "))
            if matrizJogo[linha][coluna] == 0:
                matrizImpressao[linha][coluna] = 'X'
                matrizJogo[linha][coluna] = 1
                break
            else:
                system('cls')
                print("Já jogaram nessa posição")
    else:
        while True:
            linha = int(input("Jogador 2 digite a linha que você quer colocar o O: "))
            coluna = int(input("Jogador 2 digite a coluna que você quer colocar o O: "))
            if matrizJogo[linha][coluna] == 0:
                matrizImpressao[linha][coluna] = 'O'
                matrizJogo[linha][coluna] = -1
                break
            else:
                system('cls')
                print("Já jogaram nessa posição")
        
    verificaGanhador()

    quantidadeJogada += 1

while True:
    system('cls')
    imprime()
    
    if ganhador[0] == 0 and ganhador[1] == 0:
        opcao = input("Seleciona uma das seguintes opções:\n[1] - Continuar jogando\n[2] - SAIR\nOpção: ")
    elif ganhador[0] == 1:
        system('cls')
        print("JOGADOR 1 GANHOU!!")
        opcao = '2'
    elif ganhador[1] == 1:
        system('cls')
        print("JOGADOR 2 GANHOU!!")
        opcao = '2'
        


    if opcao == '1':
        iniciaJogo()
    elif opcao == '2':
        break
    else:
        print("Opção inválida")