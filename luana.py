print("--- Operações Aritméticas ---")
a = 10
b = 3

soma = a + b          # Soma
subtracao = a - b     # Subtração
multiplicacao = a * b # Multiplicação
divisao = a / b       # Divisão (sempre retorna um número com ponto flutuante, ex: float)
divisao_inteira = a // b # Divisão inteira (descarta a parte decimal)
resto = a % b         # Resto da divisão (módulo)
potencia = a ** b     # Potência (a elevado a b)

print(f" {a}+ {b} = {soma}")
print(f"{a} - {b} = {subtracao}")
print(f"{a} * {b} = {multiplicacao}")
print(f"{a} / {b} = {divisao}")
print(f"{a} // {b} = {divisao_inteira}")
print(f"{a} % {b} = {resto}")
print(f"{a} ** {b} = {potencia}")
print("-" * 20)


#Um número somado ao seu dobro resulta em 36
# x + 2x = 36
# 3x = 36
# x = 36/3
# x = 12

x = 12
resultado = x + (2*x)
print(f" o número é {x}, e seu dobro é {2*x}. Somados, o resultado é {resultado};")