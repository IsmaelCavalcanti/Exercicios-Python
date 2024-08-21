#CONTADOR de letras que n entendi como faz
palavra = input("Digite uma palavra qualquer: ")
letras = {}

for letra in palavra:
    if letra in letras:
        letras[letra] += 1
    else:
        letras[letra] = 1

letra_comum = ""
ocorrencia_letra = 0

for letra, ocorrencias in letras.items():
    if ocorrencias > ocorrencia_letra:
        letra_comum = letra
        ocorrencia_letra = ocorrencias

print(f"A letra que apareceu mais vezes foi '{letra_comum}' com {ocorrencia_letra} ocorrências.")
