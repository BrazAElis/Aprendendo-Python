#cont = 1
#while cont <= 10: # se botar while True ele fica para sempre
    #print(cont, end=' → ')
    #cont += 1
#print('acabou')
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')
# vamo usar o break pra n precisar fazer o (s -= 999)