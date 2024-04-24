soma = 0
maior = 0
mul = 0 
for p in range(1, 5):
    print(f'{p}ª PESSOA')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    gen = str(input('Sexo [F/M]: ')).upper()
    soma += idade 
    #print(f'{soma} idade')
    # condição de genero -> homem mais velho
    #if p == 1 and gen in 'Mm': (pode ser assim tbm) 'Mm' Mai ou minúsculo
    if p == 1 and gen == 'M':
        maior = idade
    if gen == 'M' and idade > maior:
            maior = idade
    # condição de genero -> quant de mulheres -> idade < 20
    if gen == 'F' and idade < 20:
        mul += 1
        #print(mul)

print(f'A idade média do grupo é {soma/4}')
print(f'O homem mais velho tem {maior} anos')
print(f'Ao todo são {mul} mulheres com menos de 20 anos')

#idade média do gp = soma idade / quant de pessoas
# o homem mais velho
# quant de mulheres menores de 20
