r1 = input('Reta 1: ')
r2 = input('Reta 2: ')
r3 = input('Reta 3: ')

s1 = r1 + r2
s2 = r2 + r3
s3 = r3 + r1

if s1 > r3 and s2 > r1 and s3 > r2:
    print('Com essas medidas é possível fazer um triângulo!')
else:
    print('Não é possível fazer um triângulo com essas medidas.')
