mil = total = menor = cont = 0
barato = ' '
while True:
    prod = str(input('Nome do produto: '))
    valor = int(input('Preço: R$'))
    cont += 1
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    total += valor
    if valor >= 1000:
        mil += 1
    if cont == 1:
        menor = valor
        barato = prod
    else:
        if valor < menor:
            menor = valor
            barato = prod
    if r == 'N':
        break
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {mil:.2f} custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa {menor:.2f}')
