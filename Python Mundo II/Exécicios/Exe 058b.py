from random import randint
nc = randint(0, 10)

print("""Sou o seu computador...
Acabei de pensar em um número de 0 e 10.
Será que você consegue adivinhar qual foi?""")

tent = 0
nj = int(input('Qual é seu palpite? '))
while nj != nc:
    if nj < nc:
        print('Mais... tente mais uma vez!')
        nj = int(input('Qual é seu palpite? '))
        tent += 1
    else:
        print('Menos... tente mais uma vez!')
        nj = int(input('Qual é seu palpite? '))
        tent += 1
print(f'Acerto com {tent} tentativas. Parabéns!')




