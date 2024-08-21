#mostra todas as letras de uma palavra

palavra = input("Digite uma palavra: ")

letras = []

for letra in palavra:
    letras.append(letra)

print("Letras:")

for letra in letras:
    print(letra)
