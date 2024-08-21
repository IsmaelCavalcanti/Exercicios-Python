#IDENTIFICA PALAVRA FEIO e para o programa
while True:
    frase = input("Digite uma frase: ")
    print(frase)
    if "feio" in frase.lower():
        print("Palavra 'feio' encontrada. Fim do programa.")
        break
