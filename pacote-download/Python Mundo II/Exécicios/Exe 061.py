print('Gerador de PA')
print('-=-' * 10)
n1 = int(input('Primeiro termo da PA: '))
ra = int(input('Razão da PA: '))
c = n1
while c < n1 + (ra * 10):
    c += ra
    print(f'{c}', end = ' → ')
print('FIM')
# 10 primeiros termos de uma PA
# n1 + ra = n2, n2 + ra = n3 ...

# bônus
# se r > 0 (PA crescente)
# se r < 0 (PA decrescente)
# se r = 0 (PA constante)

