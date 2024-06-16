r = 'S'
n = cont = med = soma = maior = menor = 0
while r in 'Ss':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n  
    soma += n
med = soma / cont
print(f'Você digitou {cont} números e a média foi {med:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
