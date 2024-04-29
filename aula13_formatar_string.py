#f-string
nome = 'Lucas Fauth'
altura = 2.00
peso =  135
imc = peso / (altura * altura)

linha_1 =  f'{nome} tem {altura:.2f} de altura'
#                              :.2f define 2 casas após o ponto
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'
print(linha_1)
print(linha_2)
print(linha_3)