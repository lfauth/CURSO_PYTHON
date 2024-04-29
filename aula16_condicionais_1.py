#if...elfi........else
#se...se não se...se não
entrar = input(f'Você quer entrar ou sair?')

if entrar == 'entrar':
    print('Você entrou no sistema!')
elif entrar == 'sair':
    print('Você saiu do sistema!')
else:
    print('Você deve escolher uma opção!!!')

print('FORA DO IF')