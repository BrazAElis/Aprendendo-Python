p = float(input('Digite seu peso: (kg) '))

h = float(input('Digite sua altura: (m) '))

#if h.is_integer():
    #h = h / 100
        # se colocarem em cm, número inteiro

imc = p / (h**2)
    # imc = kg / m^2 


print(f'{p}kg, {h}m, imc = {imc:.1f}')

if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif 18.5 <= imc < 25:
    print('Você está no PESO IDEAL!')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO!')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')






