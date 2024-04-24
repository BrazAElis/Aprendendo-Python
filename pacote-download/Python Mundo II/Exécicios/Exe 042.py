r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))

s1 = r1 + r2
s2 = r2 + r3
s3 = r3 + r1

#d1 = s1 / 2
#d2 = s2 / 2
#d3 = s3 / 2
#if d1 == r1 and r2 or d2 == r2 and r3 or d3 == r3 and r1:
    #print('Esse triângulo é ISÓSCELES')

if r1 < s2 and r2 < s3 and r3 < s1:
    print('Com essas medidas é possível fazer um triângulo ', end='')   
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Com essas medidas não é possível fazer um triângulo.')

#elif r1 == r2 or r1 == r3 or r2 == r3:
    #print('Esse triângulo é ISÓSCELES')
