while True:
    n = int(input('Quer ver a tabuada de qual número? '))
    if n < 0:
        break
    print('-' * 36)
    for c in range(1, 11):
        print(f'{n} X {c} = {n * c}')
    print('-' * 36)
print('Número negativo. Programa encerrado.')
