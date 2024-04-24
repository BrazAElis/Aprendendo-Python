
a = input('Digite algo: ')

green = '\033[;32;40m'
red = '\033[;31;40m'
yellow = '\033[;33;40m'
limpa = '\033[m'

t = type(a)

print(f'O tipo primitivo desse valor é {yellow} {t} {limpa}')


u = a.isupper()

if u == True:
    print(f'Está em maiúcula? {green} {u} {limpa}')
else:
    print(f'Tipo primitivo desse valor é {red} {u} {limpa}')
    

l = a.islower()

if l == True:
    print(f'Está em minúsculas? {green} {l} {limpa}')
else:
    print(f'Está em minúsculas? {red} {l} {limpa}')


s = a.isspace()

if s == True:
    print(f'Tem somente espaços? {green} {s} {limpa}')
else:
    print(f'Tem somente espaços? {red} {s} {limpa}')


al = a.isalpha()   

if al == True:
    print(f'É alfabético? {green} {al} {limpa}')
else:
    print(f'É alfabético? {red} {al} {limpa}')


num = a.isnumeric()

if num == True:
    print(f'É um número? {green} {num} {limpa}')
else:
    print(f'É um número? {red} {num} {limpa}')


alph = a.isalnum()

if alph == True:
    print(f'É alfanumérico? {green} {alph} {limpa}')
else:
    print(f'É alfanumérico? {red} {alph} {limpa}')


tite = a.istitle()

if tite == True:
    print(f'Está capitalizada? {green} {tite} {limpa}')
else:
    print(f'Está capitalizada? {red} {tite} {limpa}')