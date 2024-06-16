nas = int(input('Ano que você nasceu: '))

ano = int(input('Informe o ano atual: '))

idade = ano - nas

if idade <= 9:
    print(f'Com a idade de {idade} você está na categoria MIRIM')
elif 9 < idade <= 14:
    print(f'Com a idade de {idade} você está na categoria INFANTIL')
elif 14 < idade <= 19:
    print(f'Com a idade de {idade} você está na categoria JUNIOR')
elif 19 < idade <= 20:
    print(f'Com a idade de {idade} você está na categoria SÊNIOR')
else:
    print(f'Com a idade de {idade} você está na categoria MASTER')
