# tem uma sequência -> um passo a passo
# vai ter os mesmo sentido de leitura (cima a baixo, da esq para dir) porém alguns comandos podem não serem lido se tive confições

# conjunto de passos -> algoritmo

# se -> condição (if)
# senão -> condição oposta (else)

# usar o tab -> indetação
# o que não sofre indetação acontece sempre
# o que tiver dentro (com indetação) acontece dentro de condições

# dois pontos no final da linha -> if

# if carro.esquerda: 
    # bloco True

# else:  
    # bloco False


tempo = int(input('Quantos anos tem seu carro? '))

if tempo <= 3:
    print('Seu carro tá novo!')
else:
    print('Seu carro tá velinho.')
print('--FIM--')

# se colocar (< 5) com 5 o carro tá velho, se for (<= 5) o carro está novo
# o primeiro e último comando (colado no lado esquerdo) sempre acontece, os outros podem ou não acontecer
# nunca acontece dois ao mesmo tempo

# ------parte simplificada------------

tempo = int(input('Quantos anos tem seu carro? '))
print('Carro novo' if tempo <= 3 else 'carro velho')
print('--FIM--')
