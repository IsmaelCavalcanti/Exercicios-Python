#Programa que define em que faixa vc está de acordo com a idade

idade = int(input("Digite sua idade: "))

if idade <= 12:
    print(f"Você tem {idade} anos, portanto é uma criança!")

elif 13 <= idade <= 19:
    print(f"Você tem {idade} anos, portanto é um adolescente")

elif 20 <= idade <= 59:
    print(f"Você tem {idade} anos, portanto é um adulto")

else:
    print(f"Você tem {idade} anos, portanto é um idoso! Ou está colocando uma idade absurda aqui e enganou o sistema.")