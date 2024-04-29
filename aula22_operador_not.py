#usado para inverter expressões.

senha = input('Senha: ')

if not senha:
    print('Favor informar sua senha!')
elif not senha =='123456':
    print('Senha incorreta!')
else:
    print('Senha correta!')