precounitario= float(input("digite o preco unitario do produto:"))
quantidade= float(input("digite a quantidade do produto:"))
frete= float(input("digite o frete do produto:"))
subtotal=precounitario*quantidade
total=subtotal+frete
print(f"o subtotal do produto é: {subtotal}")
print(f"o total do produto é: {total}")
