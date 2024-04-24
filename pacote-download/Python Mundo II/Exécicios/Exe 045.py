from random import randint
from time import sleep

print("""
Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
""")

itens = ('Pedra', 'Papel', 'Tesoura')

# faz uma lista para com a posição da lista o computador sortear com números

jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

computador = randint(0, 2)

print('-=' * 12)

print(f'Jogador jogou {itens[jogador]}')
print(f'Computador jogou {itens[computador]}')

print('-=' * 12)

# print(itens[computador])
# print(itens[jogador])

# 0 = PEDRA
# 1 = PAPEL 
# 2 = TESOURA

if computador == 0:
    if jogador == 1:
        print('JOGADOR VENCEU!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!')
elif computador == 1:
    if jogador == 2:
        print('JOGADOR VENCEU!')
    elif jogador == 0:
        print('COMPUTADOR VENCEU!')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!')
if computador == jogador:
    print('Temos um empate!')


