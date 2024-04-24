a = 3
b = 6
print(f'O valores são \033[1;35;40m{a}\033[m e \033[1;36;40m{b}\033[m')

print('\033[1;31;107mHello\033[m')


# se colocar 7 na primeira parte inverte as cores

nome = 'Ana'
cor1 = '\033[1;36;40m'
cor2 = '\033[m'

print(f'Olá {cor1} {nome} {cor2}')

print('Olá {} {} {}'.format('\033[1;35;40m', nome, '\033[m'))

cores = {'limpa': '\033[m',
         'azul': '\033[1;34;40m',
         'amarela': '\033[1;33;40m',
         'magenta': '\033[1;35;40m'}

print('Olá {} {} {}'.format(cores['amarela'], nome, cores['limpa']))

print('Os valores são {} {} {} e {} {} {}'.format(cores['azul'], a, cores['limpa'], cores['amarela'], b, cores['limpa']))