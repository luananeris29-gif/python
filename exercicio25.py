preco = float (input("Preço: R$ "))
opcao = int(input("Opção: "))

if opcao == 1:
    valor_final = preco * 0.90 
    print ("dinheiro ou pix")
elif opcao == 2:
    valor_final = preco * 0.95
    print ("débito")
elif opcao == 3: 
    valor_final = preco
    print ("credito à vista")
elif opcao == 4:
    valor_final = preco * 1.08 
    print ("credito parcelado")
else:
    valor_final = preco
    print ("Opção Válida")

print(f"Valor final: R$ {valor_final:.2f}".replace('.', ','))
