#mostra as letras de uma palavra horizontalmente

palavra = input("Digite uma palavra qualquer: ")
letras = []

for letra in palavra:
    letras.append(letra)

print("\nLetras da palavra: ")
for letra in letras:
    print(letra, end=" ")