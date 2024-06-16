from random import randint
comp = randint(1, 10)
vitoj = 0
while True:
    jog = int(input('Digite um número: '))
    soma = jog + comp
    esco = ' '
    while esco not in 'PI':
        esco = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jog} e o computador {comp}. Total de {soma}', end = ' ' )
    print('DEU PAR' if soma % 2 == 0 else ' DEU ÍMPAR')
    if esco == 'P':
        if soma % 2 == 0: 
            print('Você VENCEU!')
        else:
            print('Você PERDEU!')
            break
    if esco == 'I':
        if soma % 2 == 1:
            print('Você VENCEU!')
        else:
            print('Você PERDEU!')
            break
print(f'GAME OVER! Você venceu {vitoj} vezes')