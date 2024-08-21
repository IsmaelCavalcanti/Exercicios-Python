#Programa que diz se o caractere digitado é vogal, consoante ou "inválido"/não é uma letra

caractere = str(input("Digite uma letra: ")).lower()

match caractere:
    case "a" | "e" | "i" | "o" |"u" :
        print(f"A letra {caractere} é uma vogal")
    
    case _ if caractere.isalpha() and caractere not in ["a", "e", "i", "o", "u"] : # Verifica se o caractere digitado é uma letra 
        print(f"A letra {caractere} é uma consoante")                              # Se ele não estiver entre o array, é uma consoante
    
    case _:
        print(f"{caractere} NÃO é uma letra, filho da puta!")