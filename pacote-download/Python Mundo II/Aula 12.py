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

# ----------------- AULA 10 -------------------

# se -> condição (if) 
# senão se -> 3 caminho (elif)
# senão -> condição oposta (else)

# elif e else são opcionais, até quando usamos elif o eslse é opcional

# se -> 1 caminho 'condição' (if) 
# bloco 1
# senão se -> 3 caminho (elif)
# bloco 2
# senão se -> 4 caminho (elif)
# bloco 3
# senão -> 2 caminho 'condição oposta' (else)
# bloco 4

# dentro de um 'if' podemos usar vários 'elif'

nome = str(input('Qual é o seu nome? '))

if nome == 'Ana':
    print('Que nome bonito')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Amanda Jéssica Camila Beatriz':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal. ')
print(f'Tenha um bom dia, {nome}!')

# se colocar Ana aparece o da condição 'if' e não do 2 'elif'

# estrutura condicional aninhada
