p = float(input('Digite seu peso: (kg) '))

h = float(input('Digite sua altura: (m) '))

ida = int(input('Digite sua idade: '))

gen = input('Digite seu gênero biológico, M (masculino), F (feminino): ')

imc = p / (h**2)
    # imc = kg / m^2 

print(f'{p}kg, {h}m, imc = {imc:.1f}')



    






#if imc <= 18.5:
    #print('ABAIXO DO PESO')
#elif 18.5 < imc <= 25:
    #print('PESO IDEAL')
#elif 25 < imc <= 30:
    #print('SOBREPESO')
#elif 30 < imc <= 40:
    #print('OBESIDADE')
#else:
    #print('OBESIDADE MÓRBIDA')