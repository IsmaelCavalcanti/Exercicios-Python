#contagem regressiva usando range

numero = int(input("Digite um número: "))

if numero > 0:
    for n in range(numero, -1, -1):
       print(n)

else:
    print(f"Você digitou {numero}")