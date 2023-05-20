entrada = input("Digite um valor entre 0 e 100: ");
numero = int(entrada);


if not 0 < numero < 100:
    print("O número digitado é inválido.");
else:
    if numero % 2 == 0:
        print("O número digitado é par.");

    elif numero % 2 != 0:
        print("O número digitado é ímpar."); 