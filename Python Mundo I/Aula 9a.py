# frase = cadeia de caracteres ou texto, também porde ser strings

frase = 'Curso em Vídeo Python' 
    # 21 caracteres [0,20]

print(frase[9])
    # fatiamento mais simples
    # seria o décimo caracter

print(frase[9:13])
    # vai do 9 até o 13 mas o 13 não é incluído (sempre um a menos no final)
    # 9 ≤ x < 13

print(frase[9:21])


print(frase[9:21:2])
    # vai de 9 até 20 pulando de 2 em dois -> V(í)d(e)o()P(y)t(n)o -> VdoPto

print(frase[:5])
    # do 0 até 4, sem número começa do 0
    # pode ser : [5:]

print(frase[15:])
    # vai do 15 até 20
    # mesma coisa do exe. [9:21]

print(frase[9::3])
    # do 9 até 20 pulando de 3 em 3 -> V(í)(d)e(o)()P(y)(t)h(o)(n) -> VePh

comprimento_frase = len(frase)
    # len vem de lenth -> comprimento

print(comprimento_frase)

contagem1 = frase.count('o')
    # quantas vezes aparece 'o' na frase
    # ou só mostra as maiúsculas ou só as minúsculas

print(contagem1)

contagem2 = frase.upper().count('O')

print(contagem2)

contagem3 = frase.count('o',0,13)
    # contagem com fatiamento
    # vê quantos 'o' tem do 0 até o 12

print(contagem3)

encontrar = frase.find('deo')
    # posição do 'deo', começa na posição 11
    # se colocar um string que não existe o resultado é -1

print(encontrar)

existe = 'curso' in frase
    # é um operador, diz se tem ou não tem 

print(existe)

substituir = frase.replace('Python','Android')
    # ele prcura por Python e substitui por Android
    # ele não muda necessariamente a string, substitui de forma secundária

print(substituir)


maiúscula = frase.upper()
    # deixa em maiúsculo
    # upper é um  método então precisa dos ()
    # o que está em maiúsculo se mantém

print(maiúscula)

minúscula = frase.lower()
    # deixa em minúsculo
    # upper é um  método então precisa dos ()
    # o que está em minúsculo se mantém

print(minúscula)

cap = frase.capitalize()
    # deixa a primeira letra em maiúsculo e o resto em minúsculo

print(cap)

title = frase.title()
    # ele analisa quantas palavras tem na frase pela posição dos espaços
    # ele deixa a primeira letra de cada palavra maiúscula

print(title)






