a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))


if a < b < c :
    print(f'{a} é menor que {b} que é menor que {c}.')
if a < c < b:
    print(f'{a} é menor que {c} que menor que {b}')

if b < a < c:
    print(f'{b} é menor que {a} que é menor que {c}')
if b < c < a:
    print(f'{b} é menor que {c} que é menor que {a}')

if c < b < a:
    print(f'{c} é menor que {b} que é menor que {a}')
if c < a < b:
    print(f'{c} que é menor que {a} que é menor que {b}')
