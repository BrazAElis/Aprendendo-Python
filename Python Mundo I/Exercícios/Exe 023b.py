n = int(input('Digite um número de 0 a 9999: '))

u = n // 1 % 10 
# n // 1 = wxyz com (% 10) só aparece z
d = n // 10 % 10
# se só dividir por 10 aparece 3 dígitos, com % 10 aparece 1, com % 100 aparece dois...
# n // 10 = wzy % 10 = y
c = n // 100 % 10
# n // 100 = wz % 10 = z
m = n // 1000 % 10
# n // 1000 = w, já mostra a milhar mas é bom colocar % 10
print(f'A unidade de {n} é {u}')
print(f'A dezena de {n} é {d}')
print(f'A centena de {n} é {c}')
print(f'A milhar de {n} é {m}')

print('Só dividindo...')

print(f'{n//1}')
print(f'{n//10}')
print(f'{n//100}')
print(f'{n//1000}')
