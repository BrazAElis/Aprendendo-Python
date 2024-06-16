# melhora do Exe 028
from random import randint

nc = randint(0,10)

nj = 1
numten = 0
while nj != nc:
    nj = int(input('Adivinhe o número: '))
    if nj != nc:
        numten += 1
print(f'O número sorteado foi {nc} e foram necessário {numten} palpites para ser acertado!')