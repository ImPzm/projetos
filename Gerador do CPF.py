from random import randint

parte_1 = randint(0,999)
parte_2 = randint(0,999)
parte_3 = randint(0,999)

tudo_junto = f'{parte_1}{parte_2}{parte_3}'

resultado = 0
contador_regressivo1 = 10

for digito_1 in tudo_junto:
    resultado += int(digito_1) * contador_regressivo1
    contador_regressivo1 -= 1

digito_1 = (resultado * 10) % 11

digito_1 = digito_1 if digito_1 <= 9 else 0

junta_tudo = f'{tudo_junto}{digito_1}'
contador_regressivo2 = 11

resultado_2 = 0
for digito_2 in junta_tudo:
    resultado_2 += int(digito_2) * contador_regressivo2
    contador_regressivo2 -= 1

digito_2 = (resultado_2 * 10) % 11

digito_2 = digito_2 if digito_1 <= 9 else 0

novo_cpf =  f'{tudo_junto}{digito_1}{digito_2}'

print(novo_cpf)