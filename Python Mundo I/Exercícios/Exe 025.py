nome = str(input('Qual seu nome completo? ')).strip()

exe = 'SILVA' in nome.upper()

print(f'Seu nome tem Silva? {exe}')

print(f'Seu nome tem Silva? {"silva" in nome.lower()}')

