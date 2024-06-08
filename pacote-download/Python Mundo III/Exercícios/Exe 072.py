cont = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    r = ' '
    while num > 20:
        print(f'Tente novamente.', end=' ')
        num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {cont[num]}')
    while r not in 'NS':
        r = str(input('Deseja continuar [S/N]: ')).strip().upper()
    if r in 'N':
        break
# print(f'Você digitou o número {cont[num - 1]}') -> isso se a contagem comessasse com 'um'
# reps = str(input('Deseja continuar [S/N]: '))


# Básico

# while True:
#     num = int(input('Digite um número entre 0 e 20: '))
#     if 0 <= num <= 20:
#         break
#     print('Tente novamente.', end = ' ')
# print(f'Você digitou o número {cont[num]}')