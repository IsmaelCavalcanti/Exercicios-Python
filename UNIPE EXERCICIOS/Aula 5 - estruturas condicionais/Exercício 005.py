#programa calculador de IMC
#Digitar altura em metros e o peso em KG

#importanto a biblioteca math
import math

#Coletando os dados do Usuário
nome = str(input("Digite seu nome: "))
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

#Calculando o IMC
imc = peso / math.pow(altura, 2)

#Agora vem os "e se", com cada condição de acordo com a tabela do IMC

if imc < 18.5:
    print(f"{nome}, você está abaixo do peso! Seu IMC é {imc:.2f} \n")
    print(f"{nome}, Você precisa se alimentar melhor!")

elif 18.5 <= imc <= 24.9:
    print(f"Parabéns, {nome}! Você está com o seu peso normal \n")
    print(f"Seu IMC é {imc:.2f}")

elif 25 <= imc <= 29.9:
    print(f"{nome}, você está um pouco acima do peso. Mas, nada que uma dieta + atividades físicas moderadas não resolvam!\n")
    print(f"Seu IMC é {imc:.2f}")

elif  30 <= imc <= 34.9:
    print(f"{nome}, você tem obesidade grau 1! Só isso já podem gerar alguns pequenos problemas de saúde, sabia? \n")
    print(f"Seu IMC é {imc:.2f}")

elif 35 <= imc <= 39.9:
    print(f"{nome}, você tem obesidade grau 2! Tá ficando bem fodido!\n")
    print(f"Seu IMC é {imc:.2f}")

else:
    print(f"{nome}, você tem obesidade grau 3! Você quer morrer? Independete de serem músculos ou gordura, isso não é bom pro seu coração \n")
    print(f"Seu IMC é {imc:.2f}")