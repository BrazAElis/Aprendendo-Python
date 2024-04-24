from random import randint
nc = randint(0, 10)

print("""Sou o seu computador...
Acabei de pensar em um número de 0 e 10.
Será que você consegue adivinhar qual foi?""")
palpites = 0
acertou = False
while not acertou: 
    nj = int(input('Qual é seu palpite? '))
    palpites += 1
    if nj == nc:
        acertou = True
    else:
        if nj < nc:
            print('Mais... tente mais uma vez!')
        elif nj > nc:
            print('Menos... tente mais uma vez!')
print(f'Você acertou com {palpites} tentativas. Parabéns!')
