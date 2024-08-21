#Escreva um programa que repete tudo o que for escrito pelo usuário. 

# aqui eu digo pro programa continuar a executar o loop de repetição até que não seja mais "verdade", ou seja, até eu dar 
# alguma instrução que o termine
while True:
    usuario = input("Digite alguma coisa (ou 'sair' para sair): ")
    
    if usuario.lower() == "sair":
        print("Você é muito chato :( ADEUS!!")
        break #quebro o laço de repetição se ele digita sair/SAIR/Sair ou qualquer coisa

    else:
        print(f"{usuario}")
    