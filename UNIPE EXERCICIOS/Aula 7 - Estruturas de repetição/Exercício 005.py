#programa que pega todas as notas e faz a média
#posso botar quantas notas forem necessárias!

notas = []

while True:
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

    continuar = input("Existem mais notas? (S para sim e N para não): ")
    if continuar.upper() == 'N':
        break

    
media = sum(notas) / len(notas) # A soma de todos os elementos da lista dividido pelo tamanho da lista!
print(f"A sua média é {media:.2f}")
