sal = float(input('Quanto você ganha? R$'))

a1 = sal * 0.1
a2 = sal * 0.15

sal2 = sal + a1

s2 = '{:,.1f}'.format(sal2)

sal3 = sal + a2

s3 = '{:,.1f}'.format(sal3)

if sal > 1250.00:
    print(f'Seu aumento foi de R${a1} totalizando R${sal2}!')
else:
    print(f'Seu aumento foi de R${a2} totalizando R${sal3}!')





