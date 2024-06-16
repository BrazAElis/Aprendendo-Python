nome = str(input('Digite seu nome completo: ')).strip()
# com str a gente transforma 'nome' numa cadeia de caracteres então a gente pode usar '.strip'

print('Analisando seu nome...')

print(f'Seu nome em maiúsculas é {nome.upper()}')

print(f'Seu nome em minúsculas é {nome.lower()}')

split = nome.split()

# print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
print(f"Seu nome ao todo tem {len(nome) - nome.count(' ')} letras")

cn0 = len(split[0])

print(f'O nome {split[0]} tem {cn0} letras')
