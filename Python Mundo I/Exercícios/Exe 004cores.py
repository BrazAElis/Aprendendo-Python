
a = input('Digite algo: ')

cores = {'green':'\033[;32;40m', 
         'red': '\033[;31;40m', 
         'limpa':'\033[m', 
         'yellow':'\033[;33;40m'}

t = type(a)

print('O tipo primitivo desse valor é {} {} {}'.format(cores['yellow'], t, cores['limpa']))


u = a.isupper()

if u == True:
    print('Está em maiúcula? {} {} {}'.format(cores['green'], u, cores['limpa']))
else:
    print('Tipo primitivo desse valor é {} {} {}'.format(cores['red'], u, cores['limpa']))

l = a.islower()

if l == True:
    print('Está em minúsculas? {} {} {}'.format(cores['green'], l, cores['limpa']))
else:
    print('Está em minúsculas? {} {} {}'.format(cores['red'], l, cores['limpa']))



