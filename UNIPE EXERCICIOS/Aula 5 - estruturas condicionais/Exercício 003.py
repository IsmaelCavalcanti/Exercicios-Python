#Escreva um programa onde o usuario digita (1 a 7) no input e o programa retorna um dia da semana. o 1 equivale ao domingo e assim
#sucessivamente. Se o usuário digitar qualquer coisa além disso, o programa retorna uma mensagem de erro.

dia = int(input("Digite um número de 1 a 7: "))

match dia:
    case 1:
        print(f"O número {dia} equivale ao primeiro dia da semana: Domingo")

    case 2:
        print(f"O número {dia} equivale ao segundo dia da semana: Segunda-Feira")

    case 3:
        print(f"O número {dia} equivale ao terceiro dia da semana: Terça-Feira")

    case 4:
        print(f"O número {dia} equivale ao quarto dia da semana: Quarta-Feira")

    case 5:
        print(f"O número {dia} equivale ao quinto dia da semana: Quinta-Feira")

    case 6:
        print(f"O número {dia} equivale ao sexto dia da semana: Sexta-Feira")

    case 7:
        print(f"O número {dia} equivale ao sétimo dia da semana: Sábado")

    case _:
        print(f"{dia} Não é válido.")