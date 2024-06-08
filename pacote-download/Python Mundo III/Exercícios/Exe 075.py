# a) quts vez o 9 aparece -  b) posição do 3 - c) quais num pares
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))

tupla = (n1, n2, n3, n4)
print(f'Você digitou os valores {tupla}')
print(f'O número 9 apareceu {tupla.count(9)} vezes')
vezes3 = tupla.count(3)
if vezes3 == 0:
    print('O número 3 não aparece')
else:
    print(f'O número 3 apareceu na {tupla.index(3)+1}ª posição')
print('O valores pares digitados foram: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')

# print('Jeito Guanabara')

# núm = n1 = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: ')))

# print(f'Você digitou os valores {núm}')
# print(f'O número 9 apareceu {tupla.count(9)} vezes')
# if 3 in núm:
#     print(f'O número 3 apareceu na {tupla.index(3)+1}ª posição')
# else:
#     print('O número 3 não aparece')
# print('O valores pares digitados foram: ', end='')
# for n in tupla:
#     if n % 2 == 0:
#         print(n, end=' ')