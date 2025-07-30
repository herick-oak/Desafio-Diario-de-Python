# [01] Soma de Dois Números

def somar(a=0,b=0):
    s = a + b
    return s

a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))

num = somar(a,b)

print(f"A soma do dois numeros é {num}.")