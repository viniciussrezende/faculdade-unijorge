import os;

def cadastrar():
    print("\n\n")
    nome = input("Digite o nome do aluno: ")
    idade = input("Digite a idade do aluno: ")
    media = input("Digite a nota média do aluno: ")

    with open("alunos.txt", "a") as alunos:
        alunos.write(f"\n{nome},{idade},{media}")

def consultar():
    
    nome = input("\n\nDigite o nome do aluno que deseja consultar: ")
    print("\nResultado da consulta:\n")
    listaNomes = []
    indice = 0
    with open("alunos.txt", "r") as alunos:
        for linha in alunos.readlines():
            linha = linha.replace("\n", "").split(",")
            if nome in linha[0]:
                listaNomes.append(linha)
                print(f"{listaNomes[indice][0]}, {listaNomes[indice][1]}, {listaNomes[indice][2]}")
                indice += 1
        if len(listaNomes) == 0:
            print("Nome não encontrado na lista.")
    input("\nAperte 'enter' para continuar.")
    print("\n")

def alterar():
    nome = input("\n\nDigite o nome do aluno que deseja alterar o registro: ")
    listaNomes = []
    numeroLinha = 0
    texto = ""
    with open("alunos.txt", "r") as alunosLeitura:
        texto = alunosLeitura.readlines()
        for linha in texto:
            linha = linha.replace("\n", "").split(",")
            if nome in linha[0]:
                listaNomes.append(linha)
                listaNomes[len(listaNomes) - 1].append(numeroLinha)
            numeroLinha += 1
        
        totalDeNomes = len(listaNomes)
        #Escolher uma das opções caso haja mais de um aluno com o mesmo nome escolhido
        if totalDeNomes == 0:
            print("\nNenhum aluno encontrado.\n")
            return
        elif totalDeNomes == 1:
            listaNomes = listaNomes[0]
        else:
            print("\nSeleciona um dos seguintes alunos para modificar: \n")
            contador = 0      
            while contador < totalDeNomes:
                print(f"Código {contador + 1} - {listaNomes[contador][0]},{listaNomes[contador][1]},{listaNomes[contador][2]}")
                contador += 1
            localizaAluno = int(input("\nDigite o código do aluno que deseja modificar: "))
            listaNomes = listaNomes[localizaAluno - 1]      
        
        print(f"\nAluno a ter o cadastro modificado será: {listaNomes[0]}\n")

        


        with open("alunos.txt", "w") as alunosEscrita:
            
            print("[1] - Para alterar o nome;")
            print("[2] - Para alterar a idade;")
            print("[3] - Para alterar a média;")
            
            try:
                entrada = int(input("\nDigite o campo que deseja alterar: "))
            except:
                entrada = 4
            
            if entrada == 1:
                novoNome = input("Digite um novo nome: ")
                novaIdade = listaNomes[1]
                novaMedia = listaNomes[2]
            elif entrada == 2:
                novaIdade = input("Digite a nova idade: ")
                novoNome = listaNomes[0]
                novaMedia = listaNomes[2]
            elif entrada == 3:
                novaMedia = input("Digite a nova média: ")
                novoNome = listaNomes[0]
                novaIdade = listaNomes[1]
            else:
                print("Opção inválida.")

            numeroLinha = 0
            for linha in texto:
                if numeroLinha == listaNomes[3]:
                    alunosEscrita.write(f"{novoNome},{novaIdade},{novaMedia}\n")
                else:
                    alunosEscrita.write(linha)
                numeroLinha += 1

def main():
    while True:     
        print("Digite uma das opções abaixo:")
        print("[1] - Cadastrar")
        print("[2] - Consultar")
        print("[3] - Alterar")
        print("[0] - Sair")

        try:
            entrada = int(input("Digite aqui a opção desejada: "))
        except:
            print("Apenas números são permitidos. Por favor, tente novamente.")
            entrada = 4

        if entrada == 1:
            cadastrar()
            os.system("cls")
        elif entrada == 2:
            consultar()
            os.system("cls")
        elif entrada == 3:
            alterar()
            os.system("cls")
        elif entrada == 0:
            break
        else:
            os.system("cls")
            print("Opção inválida.")
            
    
main()