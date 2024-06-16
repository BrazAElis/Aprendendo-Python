r = str(input('Informe seu gênero [M/F]: ')).strip().upper()[0]
while r not in'MmFf':
    r = str(input('Dados invalidos. Por favor informe seu gênero: ')).strip().upper()[0]
print(f'{r} registrado com sucesso!')


# strip -> tirar os espaços
# upper -> padronizar
# [0] -> para pegar só a primeira letra
# resposta -> fim
# resposta errada -> tentativa ->  fim

# quando é string NÃO se usa != ou == é IN