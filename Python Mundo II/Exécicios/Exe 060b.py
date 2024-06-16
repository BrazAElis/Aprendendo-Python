n = int(input('Escolha um número para calcular o fatorial: '))
c = n  # contador -> já faz a sequência de (n - 1)
f = 1 # trabalhar com uma multi limpa tem que começar com 1, diferente da soma q é com 0
print(f'Calculando {n}! = ', end = '')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')




# n! = n * (n - 1) * (n - 2) * (n - 3)... (1)!
# 5! = 5 * 4 * 3 * 2 * 1
