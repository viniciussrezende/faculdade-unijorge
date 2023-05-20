with open("teste.txt", "r") as teste:
    texto = teste.readlines()
    for linha in texto:
        print(texto.index(linha))