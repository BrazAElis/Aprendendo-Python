termos = int(input("Quantos termos você quer mostrar?: "))
cont = 1
a = 0
b = 1
while cont <= termos:
    print(f'{a}', end='')
    total = a + b
    a = b
    b = total
    print(' > ' if cont < termos else ' >> FIM', end='')
    cont+=1

#@juliocezarlima9288
    
    # mosta '>' contador < termos