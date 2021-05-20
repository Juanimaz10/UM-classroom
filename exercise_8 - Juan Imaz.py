def negative_proposition(a, b, negative):
    if a <= 0 and b <= 0 and negative is True:
        print("True")
    elif negative is False:
        if a <= 0 and b <= 0:
            print("False")
        elif a >= 0 and b >= 0:
            print("False")
        else:
            print("True")
    else:
        print("False")

negative_proposition(-5,-5,True)