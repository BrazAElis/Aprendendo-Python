maior = mul = hom = 0
while True:
    print('CADASTRE UMA PESSOA')
    idade = int(input('Idade: '))
    gener = r = ' '
    while gener not in 'MF':
        gener = str(input('Gênero [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        maior += 1
    if gener == 'M':
        hom += 1
    if gener == 'F':
        if idade < 20:
            mul += 1
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print(f'O total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo tem {hom} homens cadastrados')
print(f'E temos {mul} mulheres com menos de 20 anos')