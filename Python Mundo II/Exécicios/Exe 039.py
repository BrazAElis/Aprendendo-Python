nasc = int(input('Ano de nascimento: '))

ano = int(input('Ano atual: '))

idade = ano - nasc

alis = nasc + 18

tempo = alis - ano

tempo2 = ano - alis

print(f'Quem nasceu em {nasc} tem {idade} anos em {ano}')

if idade < 18:
    print(f'Seu alistamento será em {alis}')
    print(f'Faltam {tempo} para o alistamento')
elif idade > 18:
    print(f'Seu alistamento foi em {alis}')
    print(f'Você deveria ter se alistado há {tempo2} ano(s)')
else:
    print('Você tem que se alistar esse ano!')


# elif idade == 18:
    #print('Você tem que se alistar esse ano! ')


