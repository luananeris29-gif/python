valor_imovel = float(input("Valor do imóvel: R$ "))
salario = float(input("Salário mensal: R$ "))
anos = int(input("Prazo (anos): "))

meses = anos * 12
prestacao = valor_imovel / meses
limite = salario * 0.30

print(f"Prestação: R$ {prestacao:.2f}")
print(f"Limite (30% do salário): R$ {limite:.2f}")

if prestacao <= limite:
    print("Resultado: APROVADO")
else:
    print("Resultado: NEGADO")