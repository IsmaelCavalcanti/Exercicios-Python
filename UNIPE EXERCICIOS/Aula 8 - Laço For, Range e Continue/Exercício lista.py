lista = []

while True:
    print("\nPrograma de Lista de Convidados")
    print("1 - Adicionar convidados")
    print("2 - Remover convidados")
    print("3 - Substituir convidados")

    convidado = input("Digite o nome do convidado(ou 'cabouse' para finalizar a lista) e tecle ENTER: ")

    if convidado.lower() == 'cabouse':
        break

    lista.append(convidado)
    print(lista)