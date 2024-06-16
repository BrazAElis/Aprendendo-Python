a = input('Digite o primeiro valor: ')
b = input('Digite o segundo valor: ')
c = input('Digite o terceiro valor: ')


if a < b < c :
    print(f'{a} é menor que {b} que é menor que {c}.')
elif a < c < b:
    print(f'{a} é menor que {c} que menor que {b}')
elif b < c < a:
    print(f'{b} é menor que {c} que é menor que {a}')
elif b < a < c:
    print(f'{b} é menor que {a} que é menor que {c}')
elif c < b < a:
    print(f'{c} é menor que {b} que é menor que {a}')
else:
    print(f'{c} que é menor que {a} que é menor que {b}')