green = '\033[;32m'
red = '\033[;31m'
yellow = '\033[;33m'
limpa = '\033[m'

print(f'{limpa}')
n = int(input('Digite um númer o: '))
tot = 0

for c in range(1, n+1):
    if n % c == 0:
        print(f'{green}', end='')
        tot += 1
    else:
        print(f'{red}', end='')
    print(f'{c}', end=' ')
print(f'{limpa}')
print(f'O número {yellow}{n}{limpa} foi dividido {yellow}{tot}{limpa} vezes!')

if tot == 2:
    print(f'E por isso ele é um número {yellow}PRIMO{limpa}!')
else:
    print(f'Então ele {red}NÃO{limpa} é um número {yellow}PRIMO{limpa}.')

# print(f'\n{limpa}O número {yellow}{n}{limpa} foi dividido {yellow}{tot}{limpa} vezes')
# tot diz quantos números aquele número é divisível
