#calculadora simples em pythom que captura o nome do usuário e retorna a operação matemática escolhida de acordo cm a tabuada

numero = int(input("Escolha um número inteiro: "))
operacao_mat = int(input("Escolha uma operação matemática! 1 - adição\n2 - subtração\n3 - multiplicação\n4 - divisão:\n"))


#cases equivalentes a cada operação matemática... lá vai trabalho digitando
match operacao_mat:
    case 1:
        print("ADIÇÃO\n")
        print(f"{numero} + 1 = {numero + 1}")
        print(f"{numero} + 2 = {numero + 2}")
        print(f"{numero} + 3 = {numero + 3}")
        print(f"{numero} + 4 = {numero + 4}")
        print(f"{numero} + 5 = {numero + 5}")
        print(f"{numero} + 6 = {numero + 6}")
        print(f"{numero} + 7 = {numero + 7}")
        print(f"{numero} + 8 = {numero + 8}")
        print(f"{numero} + 9 = {numero + 9}")
        print(f"{numero} + 10 = {numero + 10}")

    case 2:
        print("SUBTRAÇÃO\n")
        print(f"{numero} - 1 = {numero - 1}")
        print(f"{numero} - 2 = {numero - 2}")
        print(f"{numero} - 3 = {numero - 3}")
        print(f"{numero} - 4 = {numero - 4}")
        print(f"{numero} - 5 = {numero - 5}")
        print(f"{numero} - 6 = {numero - 6}")
        print(f"{numero} - 7 = {numero - 7}")
        print(f"{numero} - 8 = {numero - 8}")
        print(f"{numero} - 9 = {numero - 9}")
        print(f"{numero} - 10 = {numero - 10}")

    case 3:
        print("MULTIPLICAÇÃO\n")
        print(f"{numero} x 1 = {numero * 1}")
        print(f"{numero} x 2 = {numero * 2}")
        print(f"{numero} x 3 = {numero * 3}")
        print(f"{numero} x 4 = {numero * 4}")
        print(f"{numero} x 5 = {numero * 5}")
        print(f"{numero} x 6 = {numero * 6}")
        print(f"{numero} x 7 = {numero * 7}")
        print(f"{numero} x 8 = {numero * 8}")
        print(f"{numero} x 9 = {numero * 9}")
        print(f"{numero} x 10 = {numero * 10}")

    case 4:
        print("DIVISÃO\n")
        print(f"{numero} / 1 = {numero/1}")
        print(f"{numero} / 2 = {numero/2}")
        print(f"{numero} / 3 = {numero/3}")
        print(f"{numero} / 4 = {numero/4}")
        print(f"{numero} / 5 = {numero/5}")
        print(f"{numero} / 6 = {numero/6}")
        print(f"{numero} / 7 = {numero/7}")
        print(f"{numero} / 8 = {numero/8}")
        print(f"{numero} / 9 = {numero/9}")
        print(f"{numero} / 10 = {numero/10}")

    case _:
        print("Operação Inválida!")