# algoritmo - passo a passo

# c = variavél de contagem, quantos passos dar
# in range = no período de, no alcance de, intervalo

# pt = laço c intervalo(1,10):
# for c in range(1,10):
# intervalo de 1 a 10, vai andar do bloco 1 até o 10
# 'laço' seria o 'for'

# range(1, 6) = 1 até 5, no 6 para, ignora o último
# contagem de 1 até 6, range(1,7)

from time import sleep

for c in range(0, 6):
    print('oi')
print('fim')

for c in range(0, 6):
    print(c)
print('fim')

for c in range(1, 7):
    print(c)
print('fim')

for c in range(6, 0):
    print(c)
print('fim')
# só mostra 'fim'
# contagem ao contrária coloca -1 

for c in range(6, 0, -1):
    print(c) 
print('fim')

for c in range(10, 0, -1):
    print(c) 
    sleep(1)
print('FELIZ ANO NOVOO!')

for c in range(0, 7, 2):
    print(c) 
print('fim')
# 0 a 6 de 2 em 2

for c in range(7, 0, -2):
    print(c) 
print('fim')
# 7 a 0 de 2 em 2

n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('fim')

# n+1 para ser o número escrito

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c2 in range(i, f+1, p):
    print(c2)
print('fim')
# dá pra fazer a tabuáda de qualquer número

# amostragem sistemática estátistica
# início = sorteio aleátorio de 1 a 9
# fim = população total
# passo = k, que seria a população/amostra
# população = 500, amostra = 50, k = 10
# 50 pessoas de 500
