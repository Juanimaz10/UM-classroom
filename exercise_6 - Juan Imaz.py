def makes10(a,b):
    if a == 10 or b == 10:
        return print("true")
    elif a + b == 10:
        return print("true")
    else:
        return print("false")


number1 = int(input("Insert the first number:"))
number2 = int(input("Insert the second number:"))
operation = makes10(number1, number2)
operation2 = makes10(number1, number2)
result = print("The result is:", operation2)
