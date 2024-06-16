# import -> nas primeiras linhas

# bebida -> um biblioteca

# import.bebida -> pega a biblioteca toda, todas as funiconalidades de um módulo

# from.bebida.import.(item expecífico) -> quando a gente quiser selecionar


#ceil -> arrendonda um número float pra cima ↑
#floor -> arrendoda um número float pra baixo ↓
#trunc -> truncar o númro, elemina da (,) pra frente sem arredondamento
#pow -> potência, mesmo fun dos (**)
#sqrt -> raiz quadrada (square root)
#factorial -> fatorar

# import math -> todas essas funcionalidades e mais são importadas
# from math import sqrt -> só vamos usar raiz quadrada ou 
# from math import sqrt, pow -> só raiz quadrada e potência

# ____------------___________----------------____________

#import math
#num = int(input('Digite um número: '))
#raiz = math.sqrt(num)
#print(f'A raiz de {num} é {raiz:.2f}')

# print(f'A raiz de {num} é {math.floor(raiz)}') -> vai arredondar pra baixo ↓

# _________----------------__________-----------___________

from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print(f'A raiz de {num} é {floor(raiz)}')

# quando expecifica não precisa colocar (math.)
# se é mais de um coloca (,)

