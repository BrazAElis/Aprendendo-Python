frase = 'Curso em Vídeo Python'

split = frase.split()
# divide a frase considerando os espaços
# a contagem sempre rinicia a cada palavras -> C(0); e(0); V(0); P(0)
# cada palavra vai para um nova lista
# cada lista tem enumeração -> [Curso] 0; [em] 1; [Vídeo] 2; [Python] 3

print(len(frase))

print(split)

n0 = len(split[0])
n1 = len(split[1])
n2 = len(split[2])
n3 = len(split[3])

soma = n0 + n1 + n2 + n3

print(soma)

print(split[0])

print(split[3][2])
    # mostra o a letra 2 do item 3 da lista 

join = '-'.join(split)
# se quiser espaço é só colocar um espaço em branco ali na frente > ' '

print(join)