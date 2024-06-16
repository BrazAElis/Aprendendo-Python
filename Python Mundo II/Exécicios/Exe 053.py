f = str(input('Escreva uma frase: ')).strip().upper()
# stip -> tirar os espaços
# upper -> para pradonizar

palavras = f.split()
# split -> pra separar a frase em palavras

junto = ''.join(palavras)
# join -> para juntar as palavras

# os dois (split e junto) eliminaram os espaços internos

inverso = ''
# começa vazio


for letra in range(len(junto) - 1, -1, -1):
    # len -> o tamanho das palavras juntas e inverter
    inverso += junto[letra]
    # "preencher" o inverso com o junto e o laço da letra que tem o tamanho no inverso
print(f'O inverso de {junto} é {inverso}')

if inverso == junto:
    print('A frase digitada é um PALÍNDROMO')
else: 
    print('A frase digitada não é um PALÍNDROMO')

# len(junto) - 1 -> se a palavras tem 10 letras a última é a 9, é o 0 ao 9
# -1 -> vai até o -1, antes da primeira letra
# -1 -> inverso
