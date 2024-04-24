n1 = float(input('Nota da UNI1: '))
n2 = float(input('Nota da UNI2: '))

media = (n1 + n2) / 2

nes = 12 - media


if media < 2:
    print(f'Você está na FINAL precisando de {nes} pontos')
elif media < 6:
    print(f'Você está de RECUPERAÇÃO precisando de {nes} pontos')
else: 
    print(f'Com a média {media} você está APROVADO(A)')

# só mexe na média