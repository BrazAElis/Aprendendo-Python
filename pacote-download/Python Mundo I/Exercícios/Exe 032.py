ano = int(input('Diga um ano: '))

bi = ano % 4

if bi == 0:
    print(f'{ano} é um ano bissexto!')
else:
    print(f'{ano} não é um ano bissexto.')

