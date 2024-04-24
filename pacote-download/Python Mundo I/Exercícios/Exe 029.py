velo = int(input('Qual a velocidade do carro: '))

exe = velo - 80

multa = exe * 7

if velo >= 80:
    print('Você foi multado.')
    print(f'Terá que pagar {multa} em multa.')
else:
    print('Pode ficar tranquilo(a) não teve multa!')


