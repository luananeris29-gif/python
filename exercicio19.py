valor1 = float(input("primeiro valor"))
valor2 = float(input("segundo valor:"))
valor3 = float(input("terceiro valor:"))

#maior
if valor1> valor2 and valor1> valor3:
      maior = valor1
      
elif valor2> valor1 and valor2> valor3:
    maior = valor2
else:
    maior = valor3

#menor
if valor1 < valor2 and valor1 < valor3:
        menor = valor1
elif valor2 <valor1 and valor2 < valor3:
        menor = valor2
else: 
        menor =valor3
print("maior valor:",maior)
print ("menor valor:",menor)