n = c = s = 0
while True:
    n = int(input('Digite um número [999 parar]: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'{c} números foram digitados e sua soma é {s}')
# o break tem que ser antes do contador e da soma
