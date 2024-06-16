from random import randint
comp = randint(1, 10)
jog = soma = vitoj = vitoc = 0
while True:
    jog = int(input('Digite um número: '))
    esco = ' '
    soma = jog + comp
    while esco not in 'PI':
        esco = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
    if soma % 2 == 0:
        print(f'Você jogou {jog} e o computador {comp}. Total de {soma} DEU PAR')
        if esco == 'P':
            print('Você VENCEU!')
            vitoj += 1
        else:
            print('Você PERDEU!')
            vitoc += 1
    if soma % 2 == 1:
        print(f'Você jogou {jog} e o computador {comp}. Total de {soma} DEU ÍMPAR')
        if esco == 'I':
            print('Você VENCEU!')
            vitoj += 1
        else:
            print('Você PERDEU!')
            vitoc += 1
    if vitoc == 1:
        break
print(f'GAME OVER! Você venceu {vitoj} vezes')