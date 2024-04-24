nome = str(input('Digite seu nome: ')).strip().title()

print(f'Muito prazer em lhe conhecer, {nome}!')

split = nome.split()

print(f'Seu primeiro nome é {split[0]}')

print(f'Seu último nome é {split[-1]}')



