soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c, end = ' ')
        soma += c
        cont += 1
print(f'A soma dos {cont} valores solicitados é {soma}')

# se tirar o 'cont' da identação do if ele mostra 250 que é a quant de número ímpares
