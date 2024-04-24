print('Gerador de PA')
print('-=-' * 10)
n1 = int(input('Primeiro termo da PA: '))
ra = int(input('Razão da PA: '))
n = n1
c = 1
mais = 10 # sempre vai começar com 10
total = 0 
while mais != 0:
    total += mais
    while c <= total: # teve que criar esse 'total' pq a pessoa pode pedir mais termos
        n += ra
        c += 1
        print(f'{n}', end=' → ')
    print('PAUSA')
    mais = int(input('Quantos termos vc quer ver mais? '))
print(f'PA finalizada com o total de {total} termos.')
