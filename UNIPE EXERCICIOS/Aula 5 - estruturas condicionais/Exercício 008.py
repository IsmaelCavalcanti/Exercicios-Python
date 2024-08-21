#programa que recebe 3 comprimentos de lado e verifica se podemos formar um triangulo
#caso possível, verificar se é escaleno, isósceles ou equilátero


#Recebe os lados
lado1 = float(input("Digite o valor do primeiro lado: "))
lado2 = float(input("Digite o valor do segundo lado: "))
lado3 = float(input("Digite o valor do terceiro lado: "))


#Verifica se pode formar um triângulo

if (lado1 + lado2 < lado3) or (lado1 + lado3 < lado2) or (lado2 + lado3 < lado1):
    print("Não é possível formar um triângulo!")

#passada a verificação, agr ele vê qual a tipagem do triângulo

elif lado1 == lado2 == lado3:
    print("O triângulo possui 3 lados iguais, portanto é um equilatero!")

elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("O triângulo possui dois lados iguais, portanto é um isósceles!")

else:
    print("O triângulo possui 3 lados diferentes, portanto é um escaleno")