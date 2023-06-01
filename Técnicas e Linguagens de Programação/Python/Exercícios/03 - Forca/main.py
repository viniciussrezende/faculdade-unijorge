from random import choice

escolhas = ['PALAVRA', 'OUTRA', 'COMPUTADOR', 'NOVAMENTE', 'FACULDADE']

palavraEscolhida = choice(escolhas)

palavraEscolhidaModificada = list('-'*len(palavraEscolhida))

print(palavraEscolhidaModificada)


