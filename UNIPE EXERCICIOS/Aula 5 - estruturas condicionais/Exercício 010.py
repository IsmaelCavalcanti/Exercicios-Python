#Função que receba um código de um produto e retorne o preço correspondente (1- A | 2- B e etc)
#PRODUTO A: R$10 | PROD B: R$20 | PROD C = R$ 30

codigo = int(input("Digite o número equivalente ao código do produto(1 a 3): "))


#match cases com as situações possíveis

match codigo:
    case 1:
        print(f"Você digitou o código {codigo}, que equivale ao Fone de Ouvido mais barato")
        print("Seu produto custará R$10,00")

    case 2:
        print(f"Você digitou o código {codigo}, que equivale ao Fone de Ouvido intermediário")
        print("Seu produto custará R$20,00")


    case 3:
        print(f"Você digitou o código {codigo}, que equivale ao Fone de Ouvido mais cairo")
        print("Seu pedido custará R$30,00")

    case _:
        print(f"O código {codigo} não equivale a nenhum produto no nosso estoque!")