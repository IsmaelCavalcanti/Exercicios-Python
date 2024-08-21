# contador de pares e ímpares

numero = int(input("Digite um número: "))

par = 0
impar = 0

for n in range(numero + 1):
    if n % 2 == 0:
        par += 1

    else:
        impar += 1

print(f"A quantidade de números pares foi de: {par}")
print(f"Quantidade de números ímpares foi de: {impar}")