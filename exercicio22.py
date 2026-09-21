nota1= float(input("digite a nota 1:"))
nota2= float(input("digite a nota 2:"))

media= (nota1 + nota2) / 2 
print ("media:", media)

if media < 5:
   print ("Situação: reprovado")
elif media >= 5 and media < 7:
     print ("Situação: recuperacao")
else:
    print ("Situação: aprovado")

