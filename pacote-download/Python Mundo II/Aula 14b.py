for c in range(1,11):
    print(c)
print('Fim')

v = 1
while v < 11:
    print(v)
    v = v + 1
print('Fim')

n = 1
while n != 0:  # isso aq seria a 'flag' ponto de parada
    n = int(input('Digite um número: '))
print('Fim')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
print('Fim')

n = 1 
par = imp = 0 
while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par += 1
    else:
        imp += 1
print(f'Você digitou {par} numeros pares e {imp} números ímpares!')

# considerando 0 nulo

n = 1 # se tirar isso, o programa roda os while de uma vez
par = imp = 0 
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0: 
        if n % 2 == 0:
            par += 1
        else:
            imp += 1
print(f'Você digitou {par} numeros pares e {imp} números ímpares!')

