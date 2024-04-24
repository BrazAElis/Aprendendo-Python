i = int(input('Primeiro termo: '))
r = int(input('Razão: '))
f = i + (10 - 1) * r

for c in range(i, f+1, r):
    print(c, end=' → ')
print('ACABOU')

# a(n) = a1 + (an - 1) * r
# a(10) = a1 + (10 - 1) * r

# 'f + 1' pode ser 'f + r' -> para ir p/ o próximo termo