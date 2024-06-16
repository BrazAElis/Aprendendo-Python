print('´´' * 20)
print('Sequência de Fibonacci')
print('´´' * 20)
n = int(input('Quantidade de termos: '))
t1 = 0
t2 = 1
print('~~' * 20)
print(f'{t1} → {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' → {t3}', end='')
    t1 = t2 # pra fazer andar por lado
    t2 = t3 ##
    cont += 1
print(' → Fim')
print('~~' * 20)

    # define o primeiro e segundo termo e mostra na tela
    # contador começa no 3, onde o laço começa
    # regra do laço -> enquanto o contador for < q os n termos pedidos
    # define o t3 como soma de t1 e t2 e mostra na tela
    # e agr faz a substituição ( t1 = t2, t2 = t3


# fibonacci -> 1, 1, 2, 3, 5, 8, 13...
# yt prof _> Fn+2 = Fn+1 + Fn
# começo -> 0 - 1

# t3 = t1 + t2 ou tn = tn-2 + tn-1

# ----------------------------
# andar pro lado
# 0 - 1 - 1 - 2 - 3 - 5 - 8
# t1 - t2 - t3

# 0 - 1 - 1 - 2 - 3 - 5 - 8
#    t1 - t2 - t3

# 0 - 1 - 1 - 2 - 3 - 5 - 8
#        t1 - t2 - t3
# ----------------------------
