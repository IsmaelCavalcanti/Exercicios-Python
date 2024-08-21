# verifica se é par ou ímpar e se o usuario digita 0(ZERO) ele encerra

while True:
    numero = int(input("Digite um número inteiro(menos 0, pois encerrará o programa): "))

    if numero == 0:
        print("Você digitou 0, portanto o programa será encerrado!")
        break

    elif numero % 2 == 0:
        print(f"O número {numero} é par!")

    else:
        print(f"O número {numero} é ímpar!")