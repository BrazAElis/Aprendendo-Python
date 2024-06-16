n1 = float(input('Digite um número: '))

n2 = float(input('Digite outro número: '))

limpa = '\033[m'
amalero = '\033[1;33;40m'
verde = '\033[1;34;40m'

if n1 > n2:
    print(f' {amalero} {n1} {limpa} é maior que {verde} {n2} {limpa}')
elif n2 > n1:
    print(f' {verde} {n2} {limpa} é maior que {amalero} {n1} {limpa} ')
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais')