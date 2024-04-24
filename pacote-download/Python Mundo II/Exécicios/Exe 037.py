n = int(input('Digite um número: '))

print('''Escolha a base de conversão do número:
           [ 1 ] converter para BINÁRIO
           [ 2 ] converter para OCTAL
           [ 3 ] converter para HEXADECIMAL''')

opção = int(input('Sua opção: '))

bi = bin(n)

oc = oct(n)

he = hex(n)

if opção == 1:
    print(f'{n} convertido para BINÁRIO é {bi[2:]}')
elif opção == 2:
    print(f'{n} convertido para OCTAL é {oc[2:]}')
elif opção == 3:
    print(f'{n} covertido para HEXADECIMAL é {he[2:]}')
else:
    print('Essa opção não existe')

print(he)

print(oc)

print(bi)