n = int(input("Número: "))

if n % 3 == 0 and n % 5 == 0:
    print("DIVISÍVEL POR 3 E 5")
elif n % 3 == 0:
    print("DIVISÍVEL APENAS POR 3")
elif n % 5 == 0:
    print("DIVISÍVEL APENAS POR 5")
else:
    print("NÃO DIVISÍVEL POR 3 NEM 5")