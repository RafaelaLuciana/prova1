print("Este programa vai te ajudar a verificar se um número é positivo, negativo ou zero.")
print("Tudo o que você precisa fazer é me fornecer um número e eu farei o resto. Vamos lá!")

numero = float(input("Digite um número:  "))

if numero >0:
    print (f"O número é positivo")
elif numero <0:
    print (f"O número é negativo!")
else:
    print (f"O número é zero")