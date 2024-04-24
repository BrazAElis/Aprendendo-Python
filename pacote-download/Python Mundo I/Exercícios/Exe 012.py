preço = float(input('O preço do alimento é: R$ '))

desconto = preço * 0.05

cor1 = '\033[1;32;40m'
limpa = '\033[m'

print(f'Com 5% de desconto o alimento fica R$ {cor1} {preço - desconto} {limpa}')

