r = cont = soma = 0
r = int(input('Digite um número [999 para parar]: '))
while r != 999:
    cont += 1
    soma += r # soma oq é colocado, não o contador
    r = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {cont} números')
print(f'A soma dos números é igual a {soma}')

# colocando 'r' fora do while ele não entra se for = 999
# ler ele fora e dentro (última linha) do while

# pode colocar {cont - 1} e {soma - 999}