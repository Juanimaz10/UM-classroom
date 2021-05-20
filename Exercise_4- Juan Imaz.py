def difference21(n):
    subtraction = 21 - n
    if n <= 21:
       return "the difference is:",subtraction
    else:
        subtraction = 21 - n
        result = (-2) * subtraction
        return(result)

number = int(input("insert a number:"))
operation = difference21(number)
result = print(operation)
