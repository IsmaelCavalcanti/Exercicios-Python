# contando do numero escolhido até 0

numero = int(input("Digite um número inteiro positivo: " ))

if numero > 0:
    while numero >= 0: #enqt o numero for maior que 0 eu vou printar na tela o numero, subrair 1 e ir printando o resultado
        print(f"{numero}")
        numero -= 1

else:
    print(f"Você digitou {numero}!! Número invalido")
    

input() #feito para poder mostrar o resultado do programa!