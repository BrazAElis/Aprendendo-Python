times = 'Athletico-PR', 'Bahia', 'Flamengo', 'Botafogo', 'São Paulo', 'Cruzeiro', 'Atlético-MG', 'Bragantino', 'Palmeiras', 'Internacional', 'Fortaleza', 'Grêmio', 'Vasco da Gama', 'Criciúma', 'Juventude', 'Corinthians', 'Fluminense', 'EC Vitória', 'Atlético-GO', 'Cuiabá'

# a lista toda -> a) 5 primeiros. b) 4 últimos. c) times em ordem alfa d) em que posição tá a Chapecoense

print('-' * 123)
print(f'Lista do Brasileirão 2024: {times}')
print('-' * 123)
print(f'O cinco primeiros times: {times[:5]}')
print('-' * 123)
print(f'Os quatro últimos: {times[-4:]}')  # ou [16:]
print('-' * 123)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-' * 123)
print(f'O Corhintians tá na {times.index("Corinthians")}º posição')
print('-' * 123)