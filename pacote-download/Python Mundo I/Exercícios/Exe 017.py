from math import sqrt, pow
co = float(input('O cateto oposto é: '))
ca = float(input('O cateto adjacente é: '))

hipo = pow(co,2) + pow(ca,2)

print(f'A hipotenusa dessa triângulo retângulo é {sqrt(hipo)}')

