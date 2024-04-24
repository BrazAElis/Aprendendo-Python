frase = '   Aprenda Python  '

strip = frase.strip()
    # remove todo espaço inútil do ínicil e do final da frase
    # o caracter A que era o 3 começa a ser o 0

print(strip)

rstrip = frase.rstrip
    # uma variação do strip -> muitas funções tem a variação r
    # só remove o lado direito (right)

print(rstrip)

lstrip = frase.lstrip()
    # só remove o lado esquerdo (left)

print(lstrip)

