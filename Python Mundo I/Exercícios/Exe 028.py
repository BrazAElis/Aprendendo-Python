import random

nc = random.randint(0,5)

np = int(input('Escolha um número de 0 a 5: '))

if nc == np:
    print('Você venceu!')
else:
    print('O computado venceu!')

print(f'O número sorteado foi {nc}!')

