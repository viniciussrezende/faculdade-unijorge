try:
    arquivo = "notas.txt";
    arq = open(arquivo, 'r');
    texto = arq.read();
except:
    print("O arquivo " + arquivo + " não foi encontrado.");