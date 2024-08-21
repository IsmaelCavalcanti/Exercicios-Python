#Programa que lê as notas, faz a média e diz se o aluno foi reprovado, ficou na final ou passou de ano

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))
media = (nota1 + nota2)/2

if media >= 7.0:
    print(f"Parabéns, você foi aprovado com {media}")

elif media < 7.0 and media >= 4.0:
    print(f"Boa sorte, filho da puta, você está na final com {media} e precisa de {7.0 - media} para passar")

else:
    print("Burro, reprovado!")