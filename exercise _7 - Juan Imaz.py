def cerca_cien(n):
    if abs(n) == 10:
        return print("true")
    elif abs(n) == 100:
        return print("true")
    elif abs(n) == 200:
        return print("true")
    else:
        return print("false")
number = int(input("Insert a number:"))
operation = cerca_cien(number)
resultado = ("El resultado es:", operation)
















