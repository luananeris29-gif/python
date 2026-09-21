a = float(input("Lado 1: "))
b = float(input("Lado 2: "))
c = float(input("Lado 3: "))

if not (a < b + c and b < a + c and c < a + b):
    print("NÃO FORMA TRIÂNGULO")
elif a == b == c:
    print("EQUILÁTERO")
elif a == b or a == c or b == c:
    print("ISÓSCELES")
else:
    print("ESCALENO")