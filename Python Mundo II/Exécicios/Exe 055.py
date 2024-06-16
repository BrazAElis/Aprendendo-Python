maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input(f'Peso da {p}ª pessoa em kg: '))
    #print(f'Essa pessoa tem {peso}kg')
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}kg')
print(f'O maior peso lido foi de {menor}kg')


# se for a primeira ocorrencia (peso, numero, etc) ela vai ser tanto o maior quanto o menor
# if p == 1: (primeira ocorrencia, no caso o peso da 1ª pessoa)
    #maior = peso
    #menor = peso
# else:
    #if peso > maior: (peso = o que eu acabei de ler; maior = o primeiro peso )
    # o "maior" acaba virando o que acabamos de ler -> maior = peso
    # maior = peso (o maior peso agr é o peso que acabei de ler)
