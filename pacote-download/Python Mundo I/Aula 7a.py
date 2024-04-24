n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2 
di = n1 // n2
e = n1 ** n2

print(f'A soma é {s}, o produto {m}, a divisão {d}, divisão inteira {di} e a exponenciação {e}')



#nome = input('Digite seu nome: ')
#print('Prazer em te conhecer {:>20}!'.format(nome))
    # {:20} -> escreve o nome em 20 espaços antes da (!)
    # {:<ou>:20} -> desloca para direita ou esquerda em 20 espaços
    # {:^20} -> centraliza em 20 espaços
    # {:=^20} -> centraliza em 20 espaços com (=) em volta

# print(f'Prazer em te conhecer {nome:=^10}!')

# print(f'A soma de {n1} e {n2} vale {n1+n2}')
    # não precisou criar outra variável para 'soma'
    # a gente cria outra se ela for ser usada em outra ocasião

# colocar divisão com duas casas {d:.2f} lê-se: dosi pontos, ponto, duas casas flutuantes

# end = '') -> colocar isso no final do primeiro print se quiser 'emendar' com o segundo ou end = '>>>'

    #print(f'A soma é {s}, o produto {m}, a divisão {d},', end = ' ')
    #print(f'divisão inteira {di} e a exponenciação {e}')

# \n -> para quebrar a linha, colocar em outra linha sem criar outro print

    # print(f'A soma é {s}, \n o produto {m}, a divisão {d}, \n divisão inteira {di} e a exponenciação {e}')
