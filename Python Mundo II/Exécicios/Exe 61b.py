print('Gerador de PA')
print('-=-' * 10)
n1 = int(input('Primeiro termo da PA: '))
ra = int(input('Razão da PA: '))
n = n1
c = 1
while c <= 10:
    n += ra
    c += 1
    print(f'{n}', end = ' → ')
print('FIM')