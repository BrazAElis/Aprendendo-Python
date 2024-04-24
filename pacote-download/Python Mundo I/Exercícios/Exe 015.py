d = float(input('Quantos dias o carro foi alugado? '))

l = float(input('Teve quantos km rodados? '))

d1 = d * 60

l1 = l * 0.15

print(f'Com {d} dias de alugeu e {l}km rodados o alugeu fica R${d1 + l1}')



d2 = float(input('Quantos dias o carro foi alugado? '))

l2 = float(input('Teve quantos km rodados? '))

d3 = d2 * 60

l3 = l2 * 0.15

cor1 = '\033[;32;40m'
cor2 = '\033[;36;40m'
limpa = '\033[m'

print(f'Com {cor2} {d2} {limpa} dias de alugeu e {cor2} {l2}km {limpa} rodados o alugeu fica {cor1} R${d3 + l3} {limpa}')
