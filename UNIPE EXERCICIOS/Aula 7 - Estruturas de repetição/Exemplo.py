#faça um programa que execute a tabuada da adição

numero = int(input("Digite um número: "))

elemento = 0

print(f"A tabuada de adição do número {numero} = ")

while elemento <= 10:
    print(f"{numero} + {elemento} = {numero + elemento}")
    elemento = elemento + 1

print("\nCABOU O PROGRAMA!")