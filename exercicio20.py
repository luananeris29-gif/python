valor1 = int(input("Primeiro valor: "))
valor2 = int(input("Segundo valor: "))
valor3 = int(input("Terceiro valor: "))

#se
if valor1 <= valor2 and valor2 <= valor3:
    print("Ordem crescente:", valor1, valor2, valor3)

#Senão,se
elif valor1 <= valor3 and valor3 <= valor2:
    print("Ordem crescente:", valor1, valor3, valor2)

elif valor2 <= valor1 and valor1 <= valor3:
    print("Ordem crescente:", valor2, valor1, valor3)

elif valor2 <= valor3 and valor3 <= valor1:
    print("Ordem crescente:", valor2, valor3, valor1)

elif valor3 <= valor1 and valor1 <= valor2:
    print("Ordem crescente:", valor3, valor1, valor2)

#Senão
else:
    print("Ordem crescente:", valor3, valor2, valor1)