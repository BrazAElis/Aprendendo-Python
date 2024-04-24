a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))

menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
# maior agr
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print(f'O menor número é {menor} e o maior {maior}')