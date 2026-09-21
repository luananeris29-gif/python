idade = int(input("Idade: "))
estudante = input("Estudante (S/N): ").strip().upper() == "S"

valor = 30.00

if idade < 12 or estudante or idade >= 60:
    valor = valor / 2

print(f"Valor do ingresso: R$ {valor:.2f}")