print('{:=^33}'.format(' MARIAS BRAZ '))

preco = float(input('Preço da compra: R$'))

print("""
FORMAS DE PAGAMENTO

[ 1 ] à vista dinheiro cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
""")

pag = int(input('Forma de pagamento: '))

if pag == 4:
    parcelas = int(input('Quantas parcelas? '))
    par = preco / parcelas
    juros = preco * 0.2
    total = preco + juros
    print(f'Sua compra será parcelada em {parcelas:.2f}x de R${par:.2f} com JUROS!')
elif pag == 1:
    total = preco - (preco * 0.1)
    print('Sua compra terá 10% de desconto!')
elif pag == 2:
    total = preco - (preco * 0.05)
    print('Sua compra terá 5% de desconto')
elif pag == 3:
    total = preco
    par1 = preco / 2
    print(f'Sua compra será parcelada em 2x de R${par1:.2f}')
print(f'Sua compra de R${preco:.2f} custará R${total:.2f} no final!')