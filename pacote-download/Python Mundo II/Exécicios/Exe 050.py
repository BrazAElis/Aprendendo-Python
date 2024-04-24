soma = 0
cont = 0

for c in range(1, 7): 
    num = int(input(f'Digite o {c} valor: '))
    # vai aparecer 'Digite um valor' 6x
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'A soma dos {cont} algarismos PARES solicitados é {soma}')
        
        
# range de 6x do input
# condição para num pares
# mostrar o n







