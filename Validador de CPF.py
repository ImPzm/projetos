cpf_enviado = str(input('Digite um número de cpf: '))
cpf_enviado1 = cpf_enviado.replace('.', '').replace('-', '')
nove_digitos = cpf_enviado1[:9]

resultado = 0
contador_regressivo1 = 10

for digito_1 in nove_digitos:
    resultado += int(digito_1) * contador_regressivo1
    contador_regressivo1 -= 1

digito_1 = (resultado * 10) % 11

digito_1 = digito_1 if digito_1 <= 9 else 0

junta_tudo = f'{nove_digitos}{digito_1}'
contador_regressivo2 = 11

resultado_2 = 0
for digito_2 in junta_tudo:
    resultado_2 += int(digito_2) * contador_regressivo2
    contador_regressivo2 -= 1

digito_2 = (resultado_2 * 10) % 11

digito_2 = digito_2 if digito_1 <= 9 else 0

novo_cpf =  f'{nove_digitos}{digito_1}{digito_2}'

if novo_cpf == cpf_enviado1:
    print('CPF Válido')
else:
    print('CPF Inválido')