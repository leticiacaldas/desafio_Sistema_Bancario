saldo = 1500
limite_saque = 3
valor_saque = ""

while True:
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Visualizar saldo")
    print("4 - Sair")

    opcao = int(input("Escolha uma das opção: "))

    if opcao == 1:
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        saldo += valor_deposito
        print("Depósito realizado com sucesso!")

    elif opcao == 2:
        if limite_saque > 0:
            valor_saque = float(input("Digite o valor a ser sacado: "))  
            if saldo >= valor_saque:
                saldo -= valor_saque
                limite_saque -= 1
                print("Saque realizado com sucesso!")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("Limite de saques atingido.")

    elif opcao == 3:
            print("Saldo atual: R$", "{:.2f}".format(saldo))
            
    elif opcao == 4:
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")