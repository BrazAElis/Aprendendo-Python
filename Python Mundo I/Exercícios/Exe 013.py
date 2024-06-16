sal1 = float(input('O salário de Leopodina era de: R$'))

rea = sal1 * 0.15

fr = sal1 + rea

sal2 = '{:,.1f}'.format(fr)

print(f'Com o reajuste salarial de aumento de 15% o salario de Leopodina é {sal2}')
