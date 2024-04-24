n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
média = (n1 + n2)/2

print(f'A sua média foi {média:.1f}!')


green = '\033[;32;40m'
red = '\033[;31;40m'
limpa = '\033[m'

if média <= 6:
    print(f'Sua media foi {red} {média} {limpa}. Se fudeu bonito! 😍')
else:
    print(f'Sua média foi {green} {média} {limpa}! Eita como tá gênio(a)!')
