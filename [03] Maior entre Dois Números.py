#Maior entre Dois Números

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

if num1 > num2:
    print(f"O numero \"{num1}\" foi o maior digitado.")

elif num1 == num2:
    print(f"Os numeros digitados foram \"{num1}\", os dois foram iguais.")

else:
    print(f"O numero \"{num2}\" foi o maior digitado.")