#simulador caixa eletrônico

saldo = 1000.00 

while True:
    print("\nBanco Unipê")
    print("\nEscolha uma opção:")
    print("1 - Saldo")
    print("2 - Saque")
    print("3 - Depósito")
    print("4 - Sair")
    
    escolha = int(input("Opção: "))

    if escolha == 1:
        print(f"Seu saldo é de R$ {saldo:.2f}")
    
    elif escolha == 2:
        saque = float(input("Escolha um valor para sacar: "))

        if saque > saldo:
            print(f"Você possui apenas R$ {saldo:.2f} na conta! Não será possível sacar R$ {saque:.2f}")

        else:
            saldo -= saque
            print(f"Você sacou R$ {saque:.2f}")
            print(f"Novo saldo de R$ {saldo:.2f}")

    elif escolha == 3:
        deposito = float(input("Insira o valor do depósito: "))
        saldo += deposito

        print(f"Novo saldo de R$ {saldo:.2f}")

    elif escolha == 4:
        print("Volte Sempre!")
        break

    else:
        print("Opção Inválida!!!!")