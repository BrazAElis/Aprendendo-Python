real = float(input('Quanto você tem na carteira atualmente? R$'))

dolar = real / 5.078

print(f'Com R${real:.2f} você tem {dolar:.2f} US$')

dolar2 = float(input('Se você ganha em dolar: US$ '))

real2 = dolar2 * 5.078

print(f'Com {dolar2} US$ você compra R${real2}')