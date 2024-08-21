#Programa que calcula desconto com base no preço
#>100 = 10% | 50 < x < 100 = 5% | x < 50 = 0



price = float(input("Digite o valor do produto em Reais: ")) #Variável com o valor do preço
desconto = float() #Variável vazia que vai receber um valor e se alterar nos "ifs" conforme o combinado do valor dos descontos


#Condições para cada caso dos preços!

if price > 100.00:
    desconto = price - (price * 0.10)

    print(f"O produto tem o valor de R${price:.2f} \n")
    print(f"O desconto vai ser de 10%, portanto o preço fica com o valor de R$ {desconto:.2f}")

elif 50 <= price <= 100:
    desconto = price - (price * 0.05)
    print(f"O produto tem o valor de R${price:.2f} \n")
    print(f"O desconto vai ser de 5%, portando o preço fica com o valor de R$ {desconto:.2f}")

else:
    print(f"O valor do produto foi de R$ {price:.2f}")
    print("Você não receberá desconto pois o produto custa menos de R$ 50,00")
