casa = int(input('Qual é o valor da casa? R$'))

sal = int(input('Quanto você ganha? R$'))

anos = int(input('Em quantos anos você vai pagar a casa? R$'))

prestação = casa / (anos * 12)

limite = sal * 0.3

print(f'Para pagar uma casa que custa {casa:.2f} em {anos} anos, a prestação será de {prestação:.2f}')

print(f'É necessário pagar {prestação:.2f} com o mínimo de {limite:.2f}')

if prestação <= limite:
    print('O empréstimo pode ser feito!')
else: 
    print('Não é possível fazer o empréstimo')
