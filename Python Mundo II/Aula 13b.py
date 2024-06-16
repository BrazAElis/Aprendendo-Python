from random import randint

# i = int(input('Início: '))
i = randint(1, 11)
print(f'O número sorteado foi {i}')
f = int(input('População: '))
n = int(input('Número de pessoas que vão ser sorteadas: '))
p = f // n

for c2 in range(i, f+1, p):
    print(c2)
print('fim')
# dá pra fazer a tabuáda de qualquer número

# amostragem sistemática estátistica
# início = sorteio aleátorio de 0 a 10
# fim = população total
# passo = k, que seria a população/amostra
# população = 500, amostra = 50, k = 10
# 50 pessoas de 500
