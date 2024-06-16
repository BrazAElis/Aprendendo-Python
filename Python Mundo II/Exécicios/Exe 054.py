green = '\033[;32m'
limpa = '\033[m'

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input(f'Em que ano a {pess}ª pessoa nasceu? '))
    idade = atual - nasc
    #print(f'essa pessoa tem {idade} anos')
    if idade < 18:
        totmenor += 1
    else:
        totmaior += 1
    
print(f'{green}Temos {totmenor} pessoas menores de 18 anos {limpa}')
print(f'{green}Temos {totmaior} pessoas maiores de 18 anos {limpa} ')


 

