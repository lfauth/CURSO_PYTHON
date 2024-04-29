primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f"Primeiro valor = '{primeiro_valor}' é maior do que segundo valor = '{segundo_valor}'")
elif primeiro_valor < segundo_valor:
    print(f"Segundo valor = '{segundo_valor}' é maior do que primeiro valor = '{primeiro_valor}'")
else:
    print('Ambos valores são iguais!')
  