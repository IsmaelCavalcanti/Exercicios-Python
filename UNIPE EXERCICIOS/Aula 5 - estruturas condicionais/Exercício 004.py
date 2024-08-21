#Verifica se o número é positivo, negativo ou neutro

numero = int(input("Digite um número: "))

if numero == 0:
    print(f"Você digitou 0, caralho! Lógico que é um número neutro.")

elif numero > 0:
    print(f"O número {numero} é positivo!")

else:
    print(f"O número {numero} é negativo.")