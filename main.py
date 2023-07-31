menu = '''
  ############Banco Python############
            [d] Depositar
            [s] Sacar
            [e] Extrato
            [q] Sair
  ####################################'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
SAQUE_LIMITE = 3


while True:

    opcao = input(f'{menu}\n')

    if opcao == 'd':
        deposito = float(input('Informe o valor do depósito: '))

        if deposito > 0:
            saldo += deposito
            extrato += f'Depósito: R$ {deposito:.2f}\n'
            print(f'O depósito no valor de R${deposito:.2f}  foi realizado com sucesso.\nSeu saldo atual é de R${saldo:.2f}')

        else:
            print('Operação inválido, tente novamente.')

    elif opcao == 's':
        saque = float(input('Digite o valor do saque: '))

        sem_saldo = saque > saldo

        limite_invalido = saque > limite

        bloqueia_saque = numero_saques >= SAQUE_LIMITE

        if sem_saldo:
            print('Saldo insuficiente para resgate.')

        elif limite_invalido:
            print(f'Valor inválido. O limite para saque é de R${limite:.2f}')

        elif bloqueia_saque:
            print('Número de saques excedido.')

        elif saque > 0:
            saldo -= saque
            numero_saques += 1
            extrato += f'Saque: R${saque:.2f}\n'

        else:
            print('Operação falhou, o valor informado é inválido.')


    elif opcao == 'e':
        print('Extrato'.center(15, '$'))
        if extrato == '':
            print('\nNão houve movimentações neste dia.\n')
        else:
            print(extrato)
        print('Extrato'.center(15, '$'))
        print(f'Saldo atual: {saldo:.2f}')

    elif opcao == 'q':
        print('Sessão finalizada.')
        break

    else:
        print('Valor inválido, tente novamente.')

