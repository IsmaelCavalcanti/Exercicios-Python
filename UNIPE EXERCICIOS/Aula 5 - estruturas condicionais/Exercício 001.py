#Escreva um programa que diga se um número é divisível por 2, 3, 5, 6 ou 7, caso contrário, informe que nao é divisível por nenhum
import time

numero = int(input('Digite um número: '))
divisor = []

print(f"Verificaremos se o número {numero} é divisível por 2, 3, 5, 6 ou 7!\n")
time.sleep(1)


if numero % 2 == 0:
    divisor.append(2)

if numero % 3 == 0:
    divisor.append(3)

if numero % 5 == 0:
    divisor.append(5)

if numero % 6 == 0:
    divisor.append(6)

if numero % 7 == 0:
    divisor.append(7)

if divisor:
    print (f"O {numero} é divisível por {divisor}")

else:
    print (f"O {numero} não é divisível por nenhum destes.")