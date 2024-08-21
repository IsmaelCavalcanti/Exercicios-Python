#faça um programa que execute a tabuada da multiplicação depois de ler um número inteiro

numero = int(input("Digite um número inteiro: "))
contador = 0

while (contador < 10):
    print(f"{numero} * {contador} = {numero * contador}")
    contador += 1

print("Isso é tudo!")