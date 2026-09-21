ano = float(input("digite o ano : "))
if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    print ("reusltado: bissexto")
else:
    print ("resultado: não bissexto") 