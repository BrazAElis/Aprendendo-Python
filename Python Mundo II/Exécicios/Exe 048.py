soma = 0
cont = 0
for c in range(3, 500, 3):
    if c % 2 == 1:
        #print(c, end=' ')
        soma += c
    cont += 1
print(f'A soma dos {cont} valores solicitados é {soma}')

# essa soma foi um acumulatório, 
# contador soma 1 normalmente, 'mais um número solicitado'
# soma += c -: soma recebe ele mesmo + c
# cont += 1 -: cont recebe ele mesmo + 1

# se tirar o 'cont' da identação do if ele mostra 166 q é a quant de números múltipos de 3

# isso lembra progressão aritmética, principalmente a quant de múltipolos de 3 ente 1 e 500