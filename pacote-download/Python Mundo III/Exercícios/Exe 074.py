# sorteio de 5 número e dizer o maior e menor número sorteado
from random import randint
tupla = (randint(1, 10), randint(1, 10), randint(
    1, 10), randint(1, 10), randint(1, 10))
print(f'Eu sorteie os valores {tupla}')
ordem = sorted(tupla)
print(f'O maior valor sorteado foi {ordem[4]}')
print(f'O menor valor sorteado foi {ordem[0]}')

print('-' * 30)

print('Jeito Guanabara')

numeros = (randint(1, 10), randint(1, 10), randint(
    1, 10), randint(1, 10), randint(1, 10))
print('Os valores sortedados foram: ', end='')
for num in numeros:
    print(f'{num}', end=' ')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
