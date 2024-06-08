lanche = ('Hámburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# TUPLAS SÃO IMUTÁVEIS
# lanche[1] = 'Refrigerante'
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])
print(lanche[-3:])
print(len(lanche))

print('-' * 30)

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
    # print(cont)

print('-' * 30)

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

print('-' * 30)

# Os dois dão o mesmo resultado
# O de cima mostra a posição
# Pra  mostrar no debaixo tem que usar enumerate

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
# tem que ter duas variáveis

print('-' * 30)

print(sorted(lanche))
# sorted = em ordem, ele não altera a tupla mas deixa em ordem

print('-' * 30)
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b  # junta a e b
# a + b != b + a
print(c)
print(len(c))
print(c.count(5))  # mostra quantos 5 tem em c
print(c.index(5))  # mostra a posição que o 5 tá em c, ele pega a primeira ocorrência, se tiver dois iguais vai mostrar a posição do primeiro
print('-' * 30)

# diferente dos vetores do java no python as tuplas aceitam dados diferentes
pessoa = ('Ana', 17, 'F', 75)
del(pessoa) # única forma de modificar a tupla é apagar ele iteira
# não dá pra fazer del(pessoa[1])